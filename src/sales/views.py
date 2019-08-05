from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import ListView

from .models import *
from .forms import *
import csv
# Create your views here.

@permission_required('sales.view_contact')
def contact_list(r):
    contacts = Contact.objects.filter(agent=r.user.profile)
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
            form.save(r.user.profile)
    form = ContactForm()
    return render(r, 'sales/create_contact.html', context={'form': form})

@permission_required('sales.delegate')
def delegate_list(r):
    if r.method == 'POST':
        c_ids = r.POST["cids"].split(",")
        agent_id = r.POST["agent"]
        if c_ids[0] is not '':
            objects = Contact.objects.filter(id__in=c_ids).update(agent=Profile.objects.get(pk=agent_id))

    contacts = Contact.objects.filter(in_sales=True)
    page = r.GET.get('page', 1)
    num = r.GET.get('num', 3)
    paginator = Paginator(contacts, num)
    try:
        contacts_paginated = paginator.page(page)
    except PageNotAnInteger:
        contacts_paginated = paginator.page(1)
    except EmptyPage:
        contacts_paginated = paginator.page(paginator.num_pages)
    return render(r, 'sales/delegate_list.html', context={'contact_list': contacts_paginated, 'agent_form':AgentForm()})


# lines = [l.decode("utf-8") for l in r.FILES["file"].readlines()]
# reader = csv.reader(lines)
# for l in reader:
#     print(l)