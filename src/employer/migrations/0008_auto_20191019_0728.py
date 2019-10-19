# Generated by Django 2.2 on 2019-10-19 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0007_auto_20190913_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='documents',
            field=models.CharField(blank=True, choices=[('Виза 3 мес', 'Виза 3 мес'), ('Виза 1 год', 'Виза 1 год'), ('Рабочая карта', 'Рабочая карта'), ('Виза 3 месяца + Карта', 'Виза 3 месяца + Карта'), ('Виза 1 год + Карта', 'Виза 1 год + Карта'), ('Биометрия + ВНЖ', 'Биометрия + ВНЖ')], max_length=200, verbose_name='Документы'),
        ),
    ]
