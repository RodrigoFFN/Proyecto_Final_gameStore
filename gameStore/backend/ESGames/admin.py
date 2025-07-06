from django.contrib import admin

from .models import (
    UserProfile,
    Videogame,
    Category,
    Cart,
    CartItem,
    Review,
    Rating,
    Library,
)

admin.site.register(UserProfile)
admin.site.register(Videogame)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(Library)
