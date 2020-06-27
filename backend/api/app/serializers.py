from rest_framework import serializers
from django.contrib.auth.models import User

from backend.app.models import Post


class UserSerialiser(serializers.ModelSerializer):
    """Сериализация пользователя"""

    class Meta:
        model = User
        fields = ("id", "username")


class PostSerializer(serializers.ModelSerializer):
    """Serializer твитов"""
    user = UserSerialiser()
    user_like = UserSerialiser(many=True)

    class Meta:
        model = Post
        fields = ("id",
                  "user",
                  "text",
                  "date",
                  "parent",
                  "like",
                  "user_like")
