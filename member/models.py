from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    REQUIRED_FIELDS = []
    email = None
    username = models.CharField(max_length=100, unique = True)
    nickname = models.CharField(max_length=100)


# board.models로 위치 옮겨야 함
"""
from django.db import models
from board.models import Movie
# Create your models here.


class Actor(models.Model):
    movie = models.ForeignKey(Movie, null = True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    character = models.CharField(max_length=255)
    image_url = models.URLField()
    
    def __str__(self):
        return self.name
"""