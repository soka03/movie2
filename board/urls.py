from django.urls import path
from .views import *

app_name = 'board'

urlpatterns=[
    path('',init_db),
    path('<int:pk>/', detail_movie),
    path('<int:pk>/comment/', comment),
    path('home/', mainpage),
    path('search/<str:name>/', searchmovie),
]