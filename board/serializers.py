# # serializers.py

# from rest_framework import serializers
# from .models import Movie, Actor, MovieActor

# class ActorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Actor
#         fields = ['name', 'character', 'image_url']

# class MovieActorSerializer(serializers.ModelSerializer):
#     actor = ActorSerializer()

#     class Meta:
#         model = MovieActor
#         fields = ['actor']

# class MovieSerializer(serializers.ModelSerializer):
#     actors = serializers.SerializerMethodField()

#     class Meta:
#         model = Movie
#         fields = [
#             'title_kor', 'title_eng', 'poster_url', 'genre', 'showtime', 
#             'release_date', 'plot', 'rating', 'director_name', 'director_image_url', 'actors'
#         ]

#     def get_actors(self, obj):
#         movie_actors = MovieActor.objects.filter(movie=obj)
#         return MovieActorSerializer(movie_actors, many=True).data
    # def create(self, validated_data):
    #     actors_data = validated_data.pop('actors')
    #     movie = Movie.objects.create(**validated_data)
    #     for actor_data in actors_data:
    #         actor, created = Actor.objects.get_or_create(**actor_data)
    #         movie.actors.add(actor)
    #     return movie


        

from rest_framework import serializers
from .models import *


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name', 'character', 'image_url']

class SaveActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name', 'character', 'image_url']

class SaveMovieSerializer(serializers.ModelSerializer):
    actors = SaveActorSerializer(many = True)
    class Meta:
        model = Movie
        fields = [
            'actors', 'title_kor', 'title_eng', 'poster_url', 'genre', 'showtime', 
            'release_date', 'plot', 'rating', 'director_name', 'director_image_url'
        ]

    def create(self, validated_data):
        actor_datas = validated_data.pop('actors')
        movie = Movie.objects.create(**validated_data)
        for actor_data in actor_datas:
            actor, created = Actor.objects.get_or_create(**actor_data)
            movie.actors.add(actor)
        return movie


class CommentSerializer(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['nickname', 'comment']
    def get_nickname(self, obj):
        return obj.user.nickname

class MovieDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = [
            'actors',
            'title_kor',
            'title_eng',
            'poster_url',
            'genre',
            'showtime',
            'release_date',
            'plot',
            'rating',
            'director_name',
            'director_image_url',
            'comments',
        ]

class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['poster_url', 'title_kor']
        
class MovieSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title_kor', 'title_eng','poster_url']