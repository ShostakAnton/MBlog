from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Post(MPTTModel):
    """"Модель записи блога"""

    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name='twits')

    text = models.TextField("Сообщение", max_length=500)
    date = models.DateTimeField("Дата", auto_now_add=True)
    # коментарий к собщению
    parent = TreeForeignKey('self',  # что бы ссылаться на другие сообщения
                             verbose_name='Твит',
                             on_delete=models.CASCADE,  # коментарии останутся в БД даже при удалении автора
                             blank=True,
                             null=True,
                             related_name='child')
    like = models.IntegerField(default=0)
    user_like = models.ManyToManyField(User, verbose_name="Кто лайкнул", related_name="users_like")

    def __str__(self):
        return '{} - {}'.format(self.id, self.user)

    class MPTTMeta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ['id']
