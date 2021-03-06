from django.urls import path, include
from .views import *

urlpatterns = [
    path('', AllTwit.as_view(), name='home'),
    path('my/', PostView.as_view(), name='posts'),
    path('like/', Like.as_view()),
    path('favorites/', PostsIfollow.as_view(), name='favorites'),
]
