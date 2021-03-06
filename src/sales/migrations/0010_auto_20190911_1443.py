# Generated by Django 2.2 on 2019-09-11 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_auto_20190905_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone2',
            field=models.CharField(blank=True, max_length=50, verbose_name='Телефон2'),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone3',
            field=models.CharField(blank=True, max_length=50, verbose_name='Телефон3'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='next_contact_date',
            field=models.DateTimeField(default='1980-01-01 12:12:12', verbose_name='Дата следующего контакта'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_main',
            field=models.CharField(max_length=50, unique=True, verbose_name='Телефон1'),
        ),
    ]
