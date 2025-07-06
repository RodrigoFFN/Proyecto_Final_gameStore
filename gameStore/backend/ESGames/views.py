from rest_framework import viewsets
from .models.cart import Cart, CartItem
from .models.category import Category
from .models.library import Library
from .models.rating import Rating
from .models.review import Review
from .models.user_profile import UserProfile
from .models.videogame import Videogame
from .serializers import (
    CartSerializer, CartItemSerializer,
    CategorySerializer, LibrarySerializer,
    RatingSerializer, ReviewSerializer,
    UserProfileSerializer, VideogameSerializer
)

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class VideogameViewSet(viewsets.ModelViewSet):
    queryset = Videogame.objects.all()
    serializer_class = VideogameSerializer
