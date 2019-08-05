from authtools.models import User
from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'sex', 'age']

    def save(self, agent, commit=True):
        inst = super(ContactForm, self).save(commit=False)
        inst.agent = agent
        if commit:
            inst.save()
            self.save_m2m()
        return inst

class AgentForm(forms.Form):

    choices = [ (i.pk, i.name) for i in User.objects.filter(groups__name='Agent')]
    agent = forms.ChoiceField(choices=choices)

