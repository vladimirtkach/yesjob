# Generated by Django 2.2 on 2019-08-01 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0008_auto_20190730_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agentnote',
            old_name='text2',
            new_name='headline',
        ),
        migrations.RenameField(
            model_name='employernote',
            old_name='text2',
            new_name='headline',
        ),
        migrations.RenameField(
            model_name='vacancynote',
            old_name='text2',
            new_name='headline',
        ),
    ]
