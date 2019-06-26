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