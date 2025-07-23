from rest_framework import serializers
from django.contrib.auth.models import User
from .models.cart import Cart, CartItem
from .models.category import Category
from .models.library import Library
from .models.review import Review
from .models.user_profile import UserProfile
from .models.videogame import Videogame
from .models.favorite import Favorite

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','last_name']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True) 

    class Meta:
        model = UserProfile
        fields = ['user', 'balance', 'address', 'phone', 'is_admin']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class VideogameSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Videogame
        fields = '__all__'
        
class CartItemSerializer(serializers.ModelSerializer):
    videogame = VideogameSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'videogame', 'quantity']

class LibrarySerializer(serializers.ModelSerializer):
    videogame = VideogameSerializer(read_only=True)
    
    class Meta:
        model = Library
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    videogame = VideogameSerializer(read_only=True)
    videogame_id = serializers.PrimaryKeyRelatedField(
        queryset=Videogame.objects.all(),
        source='videogame',
        write_only=True
    )

    class Meta:
        model = Review
        fields = ['id', 'user', 'videogame', 'videogame_id', 'comment', 'rating', 'date']

class FavoriteSerializer(serializers.ModelSerializer):
    videogame_title = serializers.ReadOnlyField(source='videogame.title')

    class Meta:
        model = Favorite
        fields = ['id', 'videogame', 'videogame_title']

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
        Cart.objects.create(user=user.userprofile)

        return user


