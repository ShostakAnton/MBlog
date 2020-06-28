from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from backend.api.app.serializers import PostSerializer
from backend.api.profiles.serializers import ProfileSer
from backend.app.models import Post
from backend.profiles.models import Profile


class ProfileUser(APIView):
    """Вывод профиля пользователя"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        ser = ProfileSer(Profile.objects.get(user=request.user))
        i_follow = Profile.objects.filter(follow=request.user).values_list('id', flat=True)
        print(i_follow)
        return Response(ser.data)


class PublicUserInfo(APIView):
    """Публичный профиль пользователя"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        obj = Post.objects.filter(user__profile__id=request.GET.get('pk'))  # все посты пользователя
        ser = PostSerializer(obj, many=True)
        return Response(ser.data)
