from django.urls import path, include
from .views import *

urlpatterns = [
    path('', PostView.as_view(), name='posts'),
    path('like/', Like.as_view()),
]



