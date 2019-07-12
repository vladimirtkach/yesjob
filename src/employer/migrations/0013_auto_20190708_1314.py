# Generated by Django 2.0.9 on 2019-07-08 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0012_employer_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactlanguages',
            name='contact_person_model',
        ),
        migrations.RemoveField(
            model_name='contactperson',
            name='employer_model',
        ),
        migrations.AddField(
            model_name='contactlanguages',
            name='slug',
            field=models.SlugField(default=True, max_length=150, unique=True),
        ),
        migrations.AddField(
            model_name='contactperson',
            name='slug',
            field=models.SlugField(default=True, max_length=150, unique=True),
        ),
    ]
