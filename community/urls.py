from django.contrib import admin
from django.urls import path, include
from board.views import *
# 만약 import blog.views <- 이렇게 되어 있는 분들은 그대로 진행해주세요!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('board.urls')),
    path('member/', include('member.urls')),
    path('member/', include('dj_rest_auth.urls')),
    path('member/signup/', include('dj_rest_auth.registration.urls')),
]