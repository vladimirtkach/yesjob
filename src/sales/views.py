from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import ListView

from .models import *
from .forms import *
import csv
# Create your views here.


def contact_list(r):
    contacts = Contact.objects.all()
    page = r.GET.get('page', 1)
    num = r.GET.get('num', 1)

    paginator = Paginator(contacts, num)
    try:
        contacts_paginated = paginator.page(page)
    except PageNotAnInteger:
        contacts_paginated = paginator.page(1)
    except EmptyPage:
        contacts_paginated = paginator.page(paginator.num_pages)
    return render(r, 'sales/contact_list.html', context={'contact_list': contacts_paginated})



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