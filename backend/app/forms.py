from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """"Форма добавление сообщения"""

    class Meta:
        model = Post
        fields = ('text',)
