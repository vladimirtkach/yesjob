from django.shortcuts import render
from .models import *
from .forms import *
import csv
# Create your views here.


def contact_list(r):
    contacts = Contact.objects.all()
    return render(r, 'sales/contacts_list.html', context={'contact_list': contacts})


def create_contact(r):
    if r.method == 'POST':
        form = ContactForm(r.POST)
        if form.is_valid():
            form.save()
    return render(r, 'sales/create_contact.html', context={'form': ContactForm()})


# lines = [l.decode("utf-8") for l in r.FILES["file"].readlines()]
# reader = csv.reader(lines)
# for l in reader:
#     print(l)