from django.db import models


class Vacancy(models.Model):
    position = models.CharField(max_length=20)
    employers_name = models.CharField(max_length=20, blank=True)
    count_workers = models.CharField(max_length=20, blank=True)
    workplace = models.CharField(max_length=20, blank=True)
    employee_start_date = models.CharField(max_length=20, blank=True)
    working_days = models.CharField(max_length=20, blank=True)
    work_schedule = models.CharField(max_length=20, blank=True)
    job_description = models.CharField(max_length=20, blank=True)
    type_of_residence = models.CharField(max_length=20, blank=True)
    type_of_residence_common = models.CharField(max_length=20, blank=True)
    salary_total = models.CharField(max_length=20, blank=True)
    average_salary_after_trial_period = models.CharField(max_length=20, blank=True)
    average_salary_for_year = models.CharField(max_length=20, blank=True)
    recruiting_contribution = models.CharField(max_length=20, blank=True)
    rewards = models.CharField(max_length=20, blank=True)
    career_opportunities = models.CharField(max_length=20, blank=True)
    overtime_hours = models.CharField(max_length=20, blank=True)
    duration_of_trial_period = models.CharField(max_length=20, blank=True)
    general_qualification_requirements = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.position


class Employer(models.Model):
    employer_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    office_address = models.CharField(max_length=50, blank=True)
    site = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.company_name


class ContactPerson(models.Model):
    contact_person_id = models.AutoField(primary_key=True)
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
    employer_id = models.AutoField(primary_key=True)


class AgentNote(Note):
    agent = models.ForeignKey(ContactPerson, on_delete=models.CASCADE)