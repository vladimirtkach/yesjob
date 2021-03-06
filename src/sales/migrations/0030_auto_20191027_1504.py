# Generated by Django 2.2 on 2019-10-27 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0029_auto_20191025_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='color',
            field=models.CharField(blank=True, max_length=20, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='lead_quality',
            field=models.IntegerField(choices=[(-2, 'Отказ'), (-1, 'Недозвон'), (0, 'Новый'), (101, 'Ящ'), (1, 'Интересно но позже'), (2, 'Другая Вакансия'), (3, 'Приоритет'), (102, 'Принимает Решение'), (4, 'Сделка')], default=0, verbose_name='Статус'),
        ),
    ]
