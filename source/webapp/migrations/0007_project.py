# Generated by Django 2.2 on 2020-08-23 09:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_task_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(max_length=2000, verbose_name='Описание')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата старта')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата закрытия')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
    ]
