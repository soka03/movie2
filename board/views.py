from django.shortcuts import render
import requests
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

@api_view(['GET'])
def init_db(request):
    url = "https://port-0-minihackathon-12-lyec0qpi97716ac6.sel5.cloudtype.app/movie"
    res = requests.get(url)
    movies = res.json()['movies']
    for movie in movies:
        serializer = SaveMovieSerializer(data=movie)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def detail_movie(request, pk):
    try: 
        movie = Movie.objects.get(pk = pk)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Movie.DoesNotExist: return Response(status=status.HTTP_404_NOT_FOUND)

    


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment(request, pk):
    try: movie = Movie.objects.get(pk=pk)
    except:
        Movie.DoesNotExist
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CommentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save(user = request.user, movie = movie)
        movieserializer = MovieDetailSerializer(movie)
        return Response(movieserializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.pagination import PageNumberPagination
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def mainpage(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    movies = Movie.objects.all()
    result_page = paginator.paginate_queryset(movies, request)
    serializer = MainPageSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def searchmovie(request, name):
    movies = Movie.objects.filter(title_kor__icontains = name)|Movie.objects.filter(title_eng__icontains = name)
    serializer = MovieSearchSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
