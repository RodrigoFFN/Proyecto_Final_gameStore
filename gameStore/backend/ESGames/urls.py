from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    CartViewSet, CartItemViewSet,
    CategoryViewSet, LibraryViewSet,
    RatingViewSet, ReviewViewSet,
    UserProfileViewSet, VideogameViewSet
)

router = DefaultRouter()
router.register(r'cart', CartViewSet)
router.register(r'cartitem', CartItemViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'library', LibraryViewSet)
router.register(r'rating', RatingViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'userprofile', UserProfileViewSet)
router.register(r'videogame', VideogameViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    # Endpoints para JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

