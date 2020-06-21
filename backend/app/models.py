from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """"Модель записи блога"""

    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,)

    text = models.TextField("Сообщение", max_length=500)
    date = models.DateTimeField("Дата", auto_now_add=True)
    # коментарий к собщению
    twit = models.ForeignKey('self',        #   что бы ссылаться на другие сообщения
                             verbose_name='Твит',
                             on_delete=models.SET_NULL,     # коментарии останутся в БД даже при удалении автора
                             blank=True,
                             null=True)
    like = models.IntegerField(default=0)

    def __str__(self):
        return '{} - {}'.format(self.id ,self.user)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ['id']