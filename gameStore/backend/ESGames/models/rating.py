from django.db import models
from .user import User
from .videogame import Videogame

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videogame = models.ForeignKey(Videogame, on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.score} - {self.user.user.email} - {self.videogame.title}"

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(score__gte=1, score__lte=5),
                name="score_between_1_and_5"
            )
        ]