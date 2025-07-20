from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from .models.cart import Cart, CartItem
from rest_framework.response import Response
from rest_framework import status
from .models.category import Category
from .models.library import Library
from .models.rating import Rating
from .models.review import Review
from .models.user_profile import UserProfile
from .models.videogame import Videogame
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (
    CartSerializer, CartItemSerializer,
    CategorySerializer, LibrarySerializer,
    RatingSerializer, ReviewSerializer,
    UserProfileSerializer, VideogameSerializer
)

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

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class VideogameViewSet(viewsets.ModelViewSet):
    queryset = Videogame.objects.all()
    serializer_class = VideogameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    address = request.data.get('address', '')
    phone = request.data.get('phone', '')

    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password, email=email)

    UserProfile.objects.create(user=user, address=address, phone=phone)

    refresh = RefreshToken.for_user(user)

    return Response({
        'message': 'User and profile created successfully.',
        'access': str(refresh.access_token),
        'refresh': str(refresh)
    }, status=status.HTTP_201_CREATED)
