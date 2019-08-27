from authtools.models import User
from django import forms
from .models import *
from datetime import date
from datetime import timedelta


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['agent', 'source', 'in_sales', 'is_client']

    def save(self, agent=None, commit=True):
        inst = super(ContactForm, self).save(commit=False)
        if agent is not None:
            inst.agent = agent
            inst.source = "agent_" + agent.user.name
        if commit:
            inst.save()
            self.save_m2m()
        return inst

class AgentForm(forms.Form):
    choices = [ (i.pk, i.name) for i in (User.objects.filter(groups__name='Agent') | User.objects.filter(groups__name='SuperAgent'))]
    agent = forms.ChoiceField(choices=choices)

class AgentStats(AgentForm):
    start_date=forms.DateField(label="Начало периода", widget=forms.TextInput(attrs={'autocomplete':'off'}),
                               initial=date.today()-timedelta(days = 15))
    end_date=forms.DateField(label="Конец периода", widget=forms.TextInput(attrs={'autocomplete':'off'}), initial=date.today())
    choices = [(i.pk, i.name) for i in
               (User.objects.filter(groups__name='Agent') | User.objects.filter(groups__name='SuperAgent'))]
    choices.insert(0, ("all","Все"))
    agent = forms.ChoiceField(choices=choices)


class ContactSourceForm(forms.Form):
        choices = [(i.pk, i.name) for i in ContactSource.objects.all()]
        source = forms.ChoiceField(choices=choices)


class InteractionForm(forms.ModelForm):
    date = forms.DateTimeField(label="Дата следующего контакта",widget=forms.TextInput(attrs={'autocomplete':'off'}))
    class Meta:
        model = Interaction
        exclude = ["agent", "interaction_date", "contact"]
        widgets = {
            'result': forms.Textarea(attrs={'cols': 60, 'rows': 15}),
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