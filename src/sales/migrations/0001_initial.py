# Generated by Django 2.2 on 2019-09-03 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=250)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('phone_main', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('age', models.IntegerField(blank=True, default=0)),
                ('sex', models.CharField(blank=True, choices=[('м', 'Мужской'), ('ж', 'Женский')], max_length=1)),
                ('is_client', models.BooleanField(default=False)),
                ('in_sales', models.BooleanField(default=False)),
                ('lead_quality', models.IntegerField(default=0)),
                ('city', models.CharField(blank=True, default='', max_length=50)),
                ('next_contact_date', models.DateTimeField(auto_now=True)),
                ('comment', models.CharField(blank=True, max_length=250)),
                ('cv_url', models.CharField(blank=True, max_length=250)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('agent', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(blank=True, max_length=200)),
                ('interaction_date', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('звонок', 'Звонок'), ('email', 'Email'), ('sms', 'Sms'), ('messenger', 'Messenger')], max_length=200)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='SkillProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Contact')),
                ('interaction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sales.Interaction')),
                ('provision_agent', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='provision_agent', to=settings.AUTH_USER_MODEL)),
                ('sale_agent', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sale_agent', to=settings.AUTH_USER_MODEL)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.Vacancy')),
            ],
        ),
        migrations.CreateModel(
            name='ContactSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('potential_profiles', models.ManyToManyField(default=None, to='sales.SkillProfile')),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='profiles',
            field=models.ManyToManyField(default=None, to='sales.SkillProfile'),
        ),
        migrations.AddField(
            model_name='contact',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.ContactSource'),
        ),
    ]
