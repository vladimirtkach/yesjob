from authtools.models import User
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from .models import *


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


class InteractionForm(forms.ModelForm):
    date = forms.DateTimeField()
    sale = forms.BooleanField()
    class Meta:
        model = Interaction
        exclude = ["agent", "interaction_date", "contact"]

    def save(self, agent, contact, commit=True):
        inst = super(InteractionForm, self).save(commit=False)
        inst.agent = agent
        inst.contact = contact
        if commit:
            inst.save()
            self.save_m2m()
        return inst

    def __init__(self, *args, **kwargs):
        #choices = kwargs.pop('choices')
        choices = (("ff","fff"),("ddd","ll"))
        super(InteractionForm, self).__init__(*args, **kwargs)
        self.fields['units'] = forms.MultipleChoiceField(choices=choices)



