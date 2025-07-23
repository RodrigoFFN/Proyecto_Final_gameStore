from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    CartViewSet, CartItemViewSet,
    CategoryViewSet, LibraryViewSet, FavoriteViewSet,
    ReviewViewSet, UserProfileViewSet, VideogameViewSet,
    RegisterView, MyProfileView, my_cart_items, recharge_balance,
    AddToCartView, UpdateCartItemView, DeleteCartItemView, checkout,
)

router = DefaultRouter()
router.register(r'cart', CartViewSet)
router.register(r'cartitem', CartItemViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'library', LibraryViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'userprofile', UserProfileViewSet)
router.register(r'videogame', VideogameViewSet)
router.register(r'favorites', FavoriteViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path('register/', RegisterView.as_view(), name='register'),
    path('my-profile/', MyProfileView.as_view(), name='my-profile'),
    path('my-cart/', my_cart_items, name='my-cart'),
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('recharge/', recharge_balance, name='recharge-balance'),
    path('checkout/', checkout, name='checkout'),
    path('update-cart-item/<int:item_id>/', UpdateCartItemView.as_view(), name='update-cart-item'),
    path('delete-cart-item/<int:item_id>/', DeleteCartItemView.as_view(), name='delete-cart-item'),

    # Endpoints para JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
