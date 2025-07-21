from rest_framework import serializers
from django.contrib.auth.models import User
from .models.cart import Cart, CartItem
from .models.category import Category
from .models.library import Library
from .models.rating import Rating
from .models.review import Review
from .models.user_profile import UserProfile
from .models.videogame import Videogame

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'address', 'phone', 'last_name']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class VideogameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videogame
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    address = serializers.CharField(write_only=True, required=False)
    phone = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'address', 'phone']
        extra_kwargs = {
            'password': {'write_only': True}
        }

def create(self, validated_data):
    address = validated_data.pop('address', '')
    phone = validated_data.pop('phone', '')
    last_name = validated_data.pop('last_name', '')

    user = User.objects.create_user(**validated_data)
    user.last_name = last_name
    user.save()

    UserProfile.objects.create(user=user, address=address, phone=phone)

    return user
