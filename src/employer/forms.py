from django import forms
from .models import *


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = '__all__'
        widgets = {
            'job_description': forms.Textarea(attrs={'cols': 50, 'rows': 12}),
            'living_conditions': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
            'requirements': forms.Textarea(attrs={'cols': 50, 'rows': 8}),
            'career_opportunities': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }


class CreateEmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'


class CreateContactPersonForm(forms.ModelForm):
    languages = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(),
                                               queryset=Language.objects.all())

    class Meta:
        model = ContactPerson
        fields = '__all__'


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = '__all__'


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = EmployerNote
        fields = '__all__'
