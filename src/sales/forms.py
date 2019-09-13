from authtools.models import User
from django import forms

from .models import *
from datetime import date
from datetime import timedelta


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ['agent', 'in_sales', 'is_client', 'created_at', 'updated_at', 'last_contact_date']

    def save(self, user, commit=True):
        inst = super(ContactForm, self).save(commit=False)
        if commit:
            inst.agent = user
            inst.save()
            self.save_m2m()
        return inst

class AgentForm(forms.Form):
    choices = [ (i.pk, i.name) for i in (User.objects.filter(groups__name='Agent') | User.objects.filter(groups__name='SuperAgent'))]
    choices.append((1, "Admin"))
    agent = forms.ChoiceField(choices=choices)

class AgentStats(AgentForm):
    start_date=forms.DateField(label="Начало периода", widget=forms.TextInput(attrs={'autocomplete':'off'}),
                               initial=date.today()-timedelta(days = 3))
    end_date=forms.DateField(label="Конец периода", widget=forms.TextInput(attrs={'autocomplete':'off'}),
                             initial=date.today()+timedelta(days = 1))
    choices = [(i.pk, i.name) for i in
               (User.objects.filter(groups__name='Agent') | User.objects.filter(groups__name='SuperAgent'))]
    choices.insert(0, ("all","Все"))
    agent = forms.ChoiceField(choices=choices)


class ContactSourceForm(forms.ModelForm):
        class Meta:
            model=ContactSource
            fields='__all__'

class InteractionForm(forms.ModelForm):
    date = forms.DateTimeField(label="Дата следующего контакта",widget=forms.TextInput(attrs={'autocomplete':'off'}))
    class Meta:
        model = Interaction
        exclude = ["agent", "interaction_date", "contact"]
        widgets = {
            'result': forms.Textarea(attrs={'cols': 65, 'rows': 10}),
        }
        labels = {
            "result": "Результат",
            "type": "Тип",
        }

    def save(self, agent, contact, commit=True):
        inst = super(InteractionForm, self).save(commit=False)
        inst.agent = agent
        inst.contact = contact
        if commit:
            inst.save()
            self.save_m2m()
        return inst

    # def __init__(self, data, choices=None, *args, **kwargs):
    #     super(InteractionForm, self).__init__(data, *args, **kwargs)
    #     self.fields['sale_position'] = forms.ChoiceField(choices=choices)

class SkillProfileForm(forms.ModelForm):
    class Meta:
        model = SkillProfile
        fields = '__all__'
