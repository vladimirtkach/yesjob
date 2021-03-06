# Generated by Django 2.2 on 2019-09-18 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0015_auto_20190916_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='color',
            field=models.CharField(blank=True, choices=[('blue', 'Синий'), ('SkyBlue', 'Голубой'), ('green', 'Зеленый'), ('yellow', 'Желтый'), ('orange', 'Оранжевый'), ('red', 'Красный')], max_length=20, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='lead_quality',
            field=models.IntegerField(choices=[(-2, 'Отказ'), (-1, 'Недозвон'), (0, 'Новый'), (1, 'Интересно'), (2, 'Другая Вакансия'), (3, 'Приоритет'), (4, 'Сделка')], default=0, verbose_name='Качество лида'),
        ),
    ]
