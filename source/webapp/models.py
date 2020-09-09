from django.contrib.auth import get_user_model
from django.utils import timezone

from django.db import models
from webapp.validators import MinLengthValidator, name_char, descriptions_validator


class Status(models.Model):
    status = models.CharField(max_length=15, verbose_name='Статус')

    def __str__(self):
        return "{}.".format(self.status)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Task_type(models.Model):
    type = models.CharField(max_length=15, verbose_name='Тип')

    def __str__(self):
        return "{}.".format(self.type)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name='Описание', validators=[name_char, MinLengthValidator(5)])
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Подробное описание',
                                   validators=[descriptions_validator])
    project = models.ForeignKey('webapp.Project', related_name='tasks', on_delete=models.CASCADE, verbose_name='Проект')
    status = models.ForeignKey('webapp.Status', related_name='statuses', on_delete=models.CASCADE, verbose_name='Статус')
    task_type = models.ManyToManyField('webapp.Task_type', related_name='types', verbose_name='Тип')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    def __str__(self):
        return "{}. {}".format(self.pk, self.title)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(max_length=2000, verbose_name='Описание')
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1,
                             related_name='projects', verbose_name='Пользователь')
    start_date = models.DateField(verbose_name='Дата старта', default=timezone.now)
    end_date = models.DateField(verbose_name='Дата закрытия', null=True, blank=True)

    def __str__(self):
        return '{}. {}'.format(self.pk, self.name)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'