# Generated by Django 2.0.9 on 2019-07-06 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0008_employer_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
    ]
