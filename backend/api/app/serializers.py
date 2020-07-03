from rest_framework import serializers
from django.contrib.auth.models import User

from backend.app.models import Post


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""

    class Meta:
        model = User
        fields = ("id", "username")


class SubCategorySerializer(serializers.ModelSerializer):
    """Serializer parent твитов"""

    class Meta:
        model = Post
        fields = ("id", "text", "child",)


class PostSerializer(serializers.ModelSerializer):
    """Serializer твитов"""
    user = UserSerializer()
    user_like = UserSerializer(many=True)
    subtweet = SubCategorySerializer(source="child", many=True, required=False)

    class Meta:
        model = Post
        fields = ("id",
                  "user",
                  "text",
                  "date",
                  "parent",
                  "like",
                  "user_like",
                  "subtweet",)


class AddTweetSerializer(serializers.ModelSerializer):
    """Добавление твита"""

    class Meta:
        model = Post
        fields = ("text",)
