from django.db import models
from .category import Category

class Videogame(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    release_date = models.DateField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image_url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title