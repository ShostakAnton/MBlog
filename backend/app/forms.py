from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """"Форма добавление сообщения"""

    class Meta:
        model = Post
        fields = ('text',)
        widgets = {'text': forms.Textarea(attrs={'cols': 80, 'rows': 2, "class": "form-control",})}
        #изменение
        # размера формы