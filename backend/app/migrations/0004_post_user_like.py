# Generated by Django 3.0.7 on 2020-06-22 05:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20200621_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_like',
            field=models.ManyToManyField(related_name='users_like', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]