# Generated by Django 2.2 on 2019-09-03 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('office_address', models.CharField(blank=True, max_length=50)),
                ('site', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_expense', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_title', models.CharField(max_length=20, verbose_name='Название вакансии')),
                ('employer_name', models.CharField(blank=True, max_length=20, verbose_name='Название работодателя')),
                ('job_description', models.CharField(blank=True, max_length=20, verbose_name='Описание работы')),
                ('requirements', models.CharField(blank=True, max_length=20, verbose_name='Требования к работнику')),
                ('employee_count', models.CharField(blank=True, max_length=20, verbose_name='Необходимое количество работников')),
                ('city', models.CharField(blank=True, max_length=20, verbose_name='Город работы')),
                ('start_date', models.DateField(blank=True, max_length=20, verbose_name='Дата старта')),
                ('working_days', models.CharField(blank=True, max_length=20, verbose_name='Дни работы')),
                ('work_schedule', models.CharField(blank=True, max_length=20, verbose_name='График работы')),
                ('living_price', models.CharField(blank=True, max_length=20, verbose_name='Стоимость проживания')),
                ('living_conditions', models.CharField(blank=True, max_length=20, verbose_name='Условия проживания')),
                ('trial_duration', models.CharField(blank=True, max_length=20, verbose_name='Длительность испытательного срока')),
                ('trial_salary', models.CharField(blank=True, max_length=20, verbose_name='Зарплата во время испытательного срока')),
                ('salary', models.CharField(blank=True, max_length=20, verbose_name='Зарплата после испытательного срока')),
                ('salary_after_year', models.CharField(blank=True, max_length=20, verbose_name='Зарплата через год')),
                ('overtime_hours', models.CharField(blank=True, max_length=20, verbose_name='Максимальное количество рабочих часов')),
                ('entering_bonus', models.CharField(blank=True, max_length=20, verbose_name='Бонус при выходе на работу')),
                ('year_bonus', models.CharField(blank=True, max_length=20, verbose_name='Годовой бонус')),
                ('career_opportunities', models.CharField(blank=True, max_length=20, verbose_name='Возможности карьерного роста')),
                ('status', models.CharField(blank=True, choices=[('active', 'Активная'), ('hold', 'Приостановленная'), ('archive', 'Архивная')], max_length=20)),
                ('documents', models.CharField(blank=True, choices=[('visa', 'Виза'), ('ecard', 'Карта'), ('visa_card', 'Виза+Карта')], max_length=20)),
                ('price', models.IntegerField(blank=True, verbose_name='Стоимость вакансии')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.Employer', verbose_name='Провайдер')),
            ],
        ),
        migrations.CreateModel(
            name='VacancyNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(blank=True, max_length=200)),
                ('text', models.CharField(blank=True, max_length=200)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.Vacancy')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoryExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_expense', models.DateField(blank=True, max_length=30)),
                ('sum_of_expense', models.IntegerField(blank=True)),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.Expenses')),
            ],
        ),
        migrations.CreateModel(
            name='EmployerNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(blank=True, max_length=200)),
                ('text', models.CharField(blank=True, max_length=200)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.Employer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('role', models.CharField(blank=True, max_length=50)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.Employer')),
                ('languages', models.ManyToManyField(to='employer.Language')),
            ],
        ),
        migrations.CreateModel(
            name='AgentNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(blank=True, max_length=200)),
                ('text', models.CharField(blank=True, max_length=200)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.ContactPerson')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
