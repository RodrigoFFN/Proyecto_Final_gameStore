from django.db import models
from .user import User
from .videogame import Videogame

class Library(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videogame = models.ForeignKey(Videogame, on_delete=models.CASCADE)
    acquired_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'videogame')

    def __str__(self):
        return f"{self.user.user.email} owns {self.videogame.title}"