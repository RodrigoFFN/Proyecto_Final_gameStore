from django.db import models
from .user import User
from .videogame import Videogame

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videogame = models.ForeignKey(Videogame, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.user.email} on {self.videogame.title}"