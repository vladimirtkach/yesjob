from django.db import models

class Vacancy(models.Model):
    employer = models.ForeignKey("Employer", on_delete=models.CASCADE, verbose_name="Провайдер")
    position_title = models.CharField(max_length=580, verbose_name="Название вакансии")
    employer_name = models.CharField(max_length=80, blank=True, verbose_name="Название работодателя")
    employer_description = models.CharField(max_length=400, blank=True, verbose_name="Описание компании работодателя")
    job_description = models.CharField(max_length=1000, blank=True, verbose_name="Описание работы")
    requirements = models.CharField(max_length=500, blank=True, verbose_name="Требования к работнику")
    employee_count = models.CharField(max_length=200, blank=True, verbose_name="Необходимое количество работников")
    employee_count_add = models.CharField(max_length=200, blank=True, verbose_name="Дополнительно - Необходимое количество работников")

    city = models.CharField(max_length=200, blank=True, verbose_name="Город работы")
    start_date = models.DateField(max_length=200, blank=True, verbose_name="Дата старта")
    start_date_add = models.CharField(max_length=200, blank=True, verbose_name="Дополнительно - Дата старта")
    working_days = models.CharField(max_length=500, blank=True, verbose_name="Дни работы")
    working_days_add = models.CharField(max_length=500, blank=True, verbose_name="Дополнительно - Дни работы")
    work_schedule = models.CharField(max_length=500, blank=True, verbose_name="График работы")
    work_schedule_add = models.CharField(max_length=500, blank=True, verbose_name="Дополнительно - График работы")
    living_price = models.CharField(max_length=200, blank=True, verbose_name="Стоимость проживания")
    living_price_add = models.CharField(max_length=200, blank=True, verbose_name="Дополнительно - Стоимость проживания")
    living_conditions = models.CharField(max_length=800, blank=True, verbose_name="Условия проживания")
    trial_duration = models.CharField(max_length=200, blank=True, verbose_name="Длительность испытательного срока")
    trial_duration_add = models.CharField(max_length=200, blank=True, verbose_name="Дополнительно - Длительность испытательного срока")
    trial_salary = models.CharField(max_length=200, blank=True, verbose_name="Зарплата во время испытательного срока")
    salary = models.CharField(max_length=200, blank=True, verbose_name="Зарплата после испытательного срока")
    salary_after_year = models.CharField(max_length=500, blank=True, verbose_name="Зарплата через год")
    overtime_hours = models.CharField(max_length=500, blank=True, verbose_name="Максимальное количество рабочих часов")
    entering_bonus = models.CharField(max_length=500, blank=True, verbose_name="Бонус при выходе на работу")
    year_bonus = models.CharField(max_length=500, blank=True, verbose_name="Годовой бонус")
    career_opportunities = models.CharField(max_length=20, blank=True, verbose_name="Возможности карьерного роста")
    status = models.CharField(max_length=200, blank=True, default="active",  verbose_name="Статус", choices=(("active","Активная"),("hold","Приостановленная"),("archive","Архивная")))
    documents = models.CharField(max_length=200, blank=True, verbose_name="Документы", choices=(("Виза 3 мес","Виза 3 мес"),("Виза 1 год","Виза 1 год"),("Рабочая карта","Рабочая карта"),
                                                                      ("Виза 3 месяца + Карта","Виза 3 месяца + Карта"),("Виза 1 год + Карта","Виза 1 год + Карта")))
    documents_add = models.CharField(max_length=200, blank=True, verbose_name="Дополнительно - Документы")
    price = models.IntegerField(verbose_name="Стоимость вакансии")
    price_add = models.CharField(verbose_name="Дополнительно - Стоимость вакансии", blank=True, max_length=200)
    for_pairs = models.BooleanField(default=False, verbose_name="Для семейных пар")
    for_pairs_add = models.CharField(max_length=200, blank=True, verbose_name="Дополнительно - Для семейных пар")

    def __str__(self):
        return self.position_title


class Employer(models.Model):
    company_name = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    office_address = models.CharField(max_length=50, blank=True)
    site = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.company_name


class ContactPerson(models.Model):
    name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    role = models.CharField(max_length=50, blank=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    languages = models.ManyToManyField('Language')

    def __str__(self):
        return self.name


class Language(models.Model):
    language = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.language


class Expenses(models.Model):
    type_of_expense = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.type_of_expense


class HistoryExpense(models.Model):
    date_of_expense = models.DateField(max_length=30, blank=True)
    sum_of_expense = models.IntegerField(blank=True)
    expense = models.ForeignKey(Expenses, on_delete=models.CASCADE)


class Note(models.Model):
    headline = models.CharField(max_length=200, blank=True)
    text = models.CharField(max_length=200, blank=True)

    class Meta:
        abstract = True


class VacancyNote(Note):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)


class EmployerNote(Note):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)


class AgentNote(Note):
    agent = models.ForeignKey(ContactPerson, on_delete=models.CASCADE)