from django.db import models
from django.contrib.auth import get_user_model
from member.models import CustomUser


class Actor(models.Model):
    name = models.CharField(max_length=255)
    character = models.CharField(max_length=255)
    image_url = models.URLField()
    

class Movie(models.Model):
    title_kor = models.CharField(max_length=255)
    title_eng = models.CharField(max_length=255)
    poster_url = models.URLField()
    genre = models.CharField(max_length=255)
    showtime = models.PositiveIntegerField()
    release_date = models.DateField()
    plot = models.TextField()
    rating = models.FloatField()
    director_name = models.CharField(max_length=255)
    director_image_url = models.URLField()
    actors = models.ManyToManyField(Actor)



class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    

