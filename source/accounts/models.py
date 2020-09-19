from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user: AbstractUser = models.OneToOneField(get_user_model(), related_name='profile',
                                              on_delete=models.CASCADE, verbose_name='Пользователь')
    github = models.CharField(max_length=100, null=True, blank=True, verbose_name='Ссылка на GitHub')
    vita = models.TextField(null=True, blank=True, verbose_name='О себе')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        permissions =  [('can_view_users', 'Может смотреть пользователей')]