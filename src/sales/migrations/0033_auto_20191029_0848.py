# Generated by Django 2.2 on 2019-10-29 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0032_auto_20191029_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='watsap',
            field=models.CharField(blank=True, max_length=50, verbose_name='Ватсап'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='telegram',
            field=models.CharField(blank=True, max_length=50, verbose_name='Телеграм'),
        ),
    ]