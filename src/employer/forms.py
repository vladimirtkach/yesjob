from django import forms
from .models import *


class VacancyForm(forms.Form):
    position = forms.CharField(max_length=20)
    employers_name = forms.CharField(max_length=20)
    count_workers = forms.CharField(max_length=20)
    workplace = forms.CharField(max_length=20)
    employee_start_date = forms.CharField(max_length=20)
    working_days = forms.CharField(max_length=20)
    work_schedule = forms.CharField(max_length=20)
    job_description = forms.CharField(max_length=20)
    type_of_residence = forms.CharField(max_length=20)
    type_of_residence_common = forms.CharField(max_length=20)
    salary_total = forms.CharField(max_length=20)
    average_salary_after_trial_period = forms.CharField(max_length=20)
    average_salary_for_year = forms.CharField(max_length=20)
    recruiting_contribution = forms.CharField(max_length=20)
    rewards = forms.CharField(max_length=20)
    career_opportunities = forms.CharField(max_length=20)
    overtime_hours = forms.CharField(max_length=20)
    duration_of_trial_period = forms.CharField(max_length=20)
    general_qualification_requirements = forms.CharField(max_length=20)


    def save(self):
        new_vacancy = Vacancy.objects.create(
            position=self.cleaned_data['position'],
            employers_name=self.cleaned_data['employers_name'],
            count_workers=self.cleaned_data['count_workers'],
            workplace=self.cleaned_data['workplace'],
            employee_start_date=self.cleaned_data['employee_start_date'],
            working_days=self.cleaned_data['working_days'],
            work_schedule=self.cleaned_data['work_schedule'],
            job_description=self.cleaned_data['job_description'],
            type_of_residence=self.cleaned_data['type_of_residence'],
            type_of_residence_common=self.cleaned_data['type_of_residence_common'],
            salary_total=self.cleaned_data['salary_total'],
            average_salary_after_trial_period=self.cleaned_data['average_salary_after_trial_period'],
            average_salary_for_year=self.cleaned_data['average_salary_for_year'],
            recruiting_contribution=self.cleaned_data['recruiting_contribution'],
            rewards=self.cleaned_data['rewards'],
            career_opportunities=self.cleaned_data['career_opportunities'],
            overtime_hours=self.cleaned_data['overtime_hours'],
            duration_of_trial_period=self.cleaned_data['duration_of_trial_period'],
            general_qualification_requirements=self.cleaned_data['general_qualification_requirements'])
        return new_vacancy