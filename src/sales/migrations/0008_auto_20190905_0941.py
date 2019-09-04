# Generated by Django 2.2 on 2019-09-05 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_auto_20190905_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='cv_title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Заголовок резюме'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='cv_url',
            field=models.CharField(blank=True, max_length=250, verbose_name='Ссылка на резюме'),
        ),
    ]
