# Generated by Django 2.2 on 2019-09-05 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0008_auto_20190905_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='last_contact_date',
            field=models.DateTimeField(default='1980-01-01 12:12:12'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='next_contact_date',
            field=models.DateTimeField(default='1980-01-01 12:12:12'),
        ),
    ]
