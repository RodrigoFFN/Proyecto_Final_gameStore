from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from io import BytesIO
from datetime import datetime
from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, SAFE_METHODS, BasePermission
from rest_framework.decorators import api_view, permission_classes, action
from .models.cart import Cart, CartItem
from .models.category import Category
from .models.library import Library
from .models.review import Review
from .models.user_profile import UserProfile
from .models.videogame import Videogame
from .models.favorite import Favorite
from decimal import Decimal
from .serializers import (
    CartSerializer, CartItemSerializer, FavoriteSerializer,
    CategorySerializer, LibrarySerializer, ReviewSerializer,
    UserProfileSerializer, VideogameSerializer, RegisterSerializer
)

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user.user == request.user

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Library.objects.filter(user=self.request.user.userprofile)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        videogame_id = self.request.query_params.get('videogame')
        if videogame_id:
            queryset = queryset.filter(videogame__id=videogame_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.userprofile)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'], url_path='library')
    def library(self, request, pk=None):
        try:
            profile = self.get_object()
            items = Library.objects.filter(user=profile)
            serializer = LibrarySerializer(items, many=True)
            return Response(serializer.data)
        except UserProfile.DoesNotExist:
            return Response({'error': 'Perfil no encontrado'}, status=404)

class VideogameViewSet(viewsets.ModelViewSet):
    queryset = Videogame.objects.all()
    serializer_class = VideogameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category_id')
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        return queryset

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class MyProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = request.user.userprofile
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)
    
class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_profile = UserProfile.objects.get(user=self.request.user)
        return Favorite.objects.filter(user_profile=user_profile)

    def perform_create(self, serializer):
        user_profile = UserProfile.objects.get(user=self.request.user)
        serializer.save(user_profile=user_profile)

class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_profile = request.user.userprofile
        user_cart, _ = Cart.objects.get_or_create(user=user_profile)
        videogame_id = request.data.get('videogame_id')
        quantity = int(request.data.get('quantity', 1))

        try:
            item, created = CartItem.objects.get_or_create(
                cart=user_cart,
                videogame_id=videogame_id,
                defaults={'quantity': quantity}
            )
            if not created:
                item.quantity += quantity
                item.save()

            return Response({'success': True}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UpdateCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, item_id):
        try:
            item = CartItem.objects.get(id=item_id, cart=request.user.userprofile.cart)
            item.quantity = int(request.data.get('quantity', 1))
            item.save()
            return Response({'success': True})
        except CartItem.DoesNotExist:
            return Response({'error': 'Item no encontrado'}, status=404)

class DeleteCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, item_id):
        try:
            item = CartItem.objects.get(id=item_id, cart=request.user.userprofile.cart)
            item.delete()
            return Response({'success': True})
        except CartItem.DoesNotExist:
            return Response({'error': 'Item no encontrado'}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recharge_balance(request):
    amount = request.data.get('amount')

    try:
        amount = Decimal(amount)
    except:
        return Response({'error': 'Monto inválido'}, status=status.HTTP_400_BAD_REQUEST)

    if amount <= 0:
        return Response({'error': 'El monto debe ser mayor que 0'}, status=status.HTTP_400_BAD_REQUEST)

    profile = request.user.userprofile
    profile.balance += amount
    profile.save()

    return Response({
        'message': f'Se ha recargado ${amount} correctamente.',
        'new_balance': str(profile.balance)
    })
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def buy_cart_items(request):
    user = request.user
    profile = user.userprofile
    cart_items = CartItem.objects.filter(cart=user.cart)

    if not cart_items.exists():
        return Response({'error': 'El carrito está vacío.'}, status=status.HTTP_400_BAD_REQUEST)

    total_price = sum(item.videogame.price * item.quantity for item in cart_items)

    if profile.balance < total_price:
        return Response({'error': 'Saldo insuficiente.'}, status=status.HTTP_400_BAD_REQUEST)

    profile.balance -= Decimal(total_price)
    profile.save()

    for item in cart_items:
        Library.objects.create(user=user, videogame=item.videogame)

    cart_items.delete()

    return Response({'message': 'Compra realizada con éxito.', 'new_balance': str(profile.balance)})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_cart_items(request):
    user_profile = request.user.userprofile
    cart, _ = Cart.objects.get_or_create(user=user_profile)
    items = CartItem.objects.filter(cart=cart)
    serializer = CartItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkout(request):
    user_profile = request.user.userprofile

    try:
        cart = Cart.objects.get(user=user_profile)
        items = CartItem.objects.filter(cart=cart).select_related('videogame')
    except Cart.DoesNotExist:
        return Response({'error': 'Carrito no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    if not items:
        return Response({'error': 'El carrito está vacío.'}, status=400)

    total_price = sum(item.videogame.price * item.quantity for item in items)

    if user_profile.balance < total_price:
        return Response({'error': 'Saldo insuficiente.'}, status=status.HTTP_400_BAD_REQUEST)

    template = get_template('boleta.html')
    html = template.render({
        'user': request.user,
        'profile': user_profile,
        'items': items,
        'total': total_price,
        'date': datetime.now().strftime('%d/%m/%Y'),
    })

    pdf_buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=pdf_buffer)
    if pisa_status.err:
        return Response({'error': 'Error al generar la boleta PDF.'}, status=500)
    pdf_buffer.seek(0)

    for item in items:
        for _ in range(item.quantity):
            Library.objects.get_or_create(user=user_profile, videogame=item.videogame)

    user_profile.balance -= Decimal(total_price)
    user_profile.save()

    items.delete()

    response = HttpResponse(pdf_buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="boleta_compra.pdf"'
    return response