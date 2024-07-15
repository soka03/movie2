from django.urls import path
from .views import *

app_name = 'board'

urlpatterns=[
    path('',init_db),
    path('list/', list_movie),
    path('<int:pk>/', detail_movie),
    path('<int:pk>/comment/', comment),
]