from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('ysa/', views.ysa, name='ysahome'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
]