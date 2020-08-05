from django.db import models


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
    title = models.CharField(max_length=200, verbose_name='Описание')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Подробное описание')
    status = models.ForeignKey('webapp.Status', related_name='statuses', on_delete=models.PROTECT, verbose_name='Статус')
    type = models.ForeignKey('webapp.Task_type', related_name='types', on_delete=models.PROTECT, verbose_name='Тип')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return "{}. {}".format(self.pk, self.title)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'