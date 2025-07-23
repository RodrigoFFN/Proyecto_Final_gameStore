from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=9, blank=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email