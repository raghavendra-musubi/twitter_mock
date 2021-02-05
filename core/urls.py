from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_tweet/', views.post_tweet, name='post_tweet'),
] 
