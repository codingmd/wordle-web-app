from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Wordle(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    word = models.TextField()
    score = models.IntegerField(default=0)
    board = models.TextField(default="""
             -----
             -----
             -----
             -----
             -----
             -----
         """)
    slug = models.SlugField(unique=True)
    class Meta:
        verbose_name_plural = 'Wordles'
