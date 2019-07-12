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
    objects = models.Manager()
    #vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=150, unique=True, default=True)
    company_name = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    office_address = models.CharField(max_length=50, blank=True)
    site = models.CharField(max_length=50, blank=True)
    contact_list = models.CharField(max_length=50, blank=True)
    employer_type = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.company_name


class ContactPerson(models.Model):
    objects = models.Manager()
    slug = models.SlugField(max_length=150, unique=True, default=True)
    name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    role = models.CharField(max_length=50, blank=True)
    employer = models.CharField(max_length=50, blank=True)
    languages = models.CharField(max_length=50, blank=True)
    #employer_model = models.ForeignKey(Employer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ContactLanguages(models.Model):
    objects = models.Manager()
    slug = models.SlugField(max_length=150, unique=True, default=True)
    contact_person = models.CharField(max_length=50, blank=True)
    language = models.CharField(max_length=50, blank=True)
    language_skill = models.CharField(max_length=50, blank=True)
    #contact_person_model = models.ForeignKey(ContactPerson, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact_person
