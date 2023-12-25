from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    # recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]


class Recipe(models.Model):
    title = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True, default=None)
    ingredients = models.TextField(null=True, default=None)
    steps = models.TextField()
    time_cook = models.IntegerField(default=1, validators=[MinValueValidator(0)])
    photo = models.ImageField(upload_to='img/', null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['title']),
        ]
