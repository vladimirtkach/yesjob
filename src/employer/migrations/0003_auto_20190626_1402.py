# Generated by Django 2.0.9 on 2019-06-26 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0002_auto_20190626_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='average_salary_after_trial_period',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='average_salary_for_year',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='career_opportunities',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='count_workers',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='duration_of_trial_period',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='employee_start_date',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='employers_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='general_qualification_requirements',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='job_description',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='overtime_hours',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='position',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='recruiting_contribution',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='rewards',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_total',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='type_of_residence',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='type_of_residence_common',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='work_schedule',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='working_days',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='workplace',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
