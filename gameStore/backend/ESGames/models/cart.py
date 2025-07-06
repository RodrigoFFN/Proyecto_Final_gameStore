from django.db import models
from .user import User
from .videogame import Videogame

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart of {self.user.user.email}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    videogame = models.ForeignKey(Videogame, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.videogame.title}"