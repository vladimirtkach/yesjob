from django import forms
from .models import *


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = '__all__'


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
