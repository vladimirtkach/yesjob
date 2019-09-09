# Generated by Django 2.2 on 2019-09-04 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='profiles',
            field=models.ManyToManyField(blank=True, default=None, to='sales.SkillProfile'),
        ),
        migrations.AlterField(
            model_name='interaction',
            name='type',
            field=models.CharField(choices=[('звонок', 'Звонок'), ('email', 'Email'), ('sms', 'Sms'), ('messenger', 'Messenger'), ('автопрозвон', 'Автопрозвон')], max_length=200),
        ),
    ]