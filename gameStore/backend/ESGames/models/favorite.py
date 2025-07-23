from django.db import models
from django.contrib.auth.models import User
from .user_profile import UserProfile
from .videogame import Videogame

class Favorite(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='favorites')
    videogame = models.ForeignKey(Videogame, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_profile', 'videogame')

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.videogame.title}"
