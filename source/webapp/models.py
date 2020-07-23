from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name='Описание')
    status = models.TextField(max_length=3000, verbose_name='Статус', default='new', choices=STATUS_CHOICES)
    completion_date = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name='Время завершения')

    def __str__(self):
        return "{}. {}".format(self.pk, self.title)