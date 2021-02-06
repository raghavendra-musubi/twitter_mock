from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_tweet/', views.post_tweet, name='post_tweet'),
    path('reply/<str:pk>/', views.reply, name='reply'),
    path('detail/<str:pk>/', views.tweet_detail, name='detail'),
] 
