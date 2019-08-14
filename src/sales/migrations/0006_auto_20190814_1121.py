# Generated by Django 2.2 on 2019-08-14 11:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_auto_20190805_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='interaction',
            name='interaction_date',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interaction',
            name='type',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
