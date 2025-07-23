from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .user_profile import UserProfile
from .videogame import Videogame

class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    videogame = models.ForeignKey(Videogame, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.user.email} on {self.videogame.title}"