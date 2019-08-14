from django.contrib.auth.decorators import permission_required
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import ListView

from .models import *
from .forms import *
import csv
# Create your views here.

@permission_required('auth.agent')
def contact_list(r):
    contacts = Contact.objects.filter(agent=r.user.profile, in_sales=True)
    page = r.GET.get('page', 1)
    num = r.GET.get('num', 50)

    paginator = Paginator(contacts, num)
    try:
        contacts_paginated = paginator.page(page)
    except PageNotAnInteger:
        contacts_paginated = paginator.page(1)
    except EmptyPage:
        contacts_paginated = paginator.page(paginator.num_pages)
    return render(r, 'sales/contact_list.html', context={'contact_list': contacts_paginated})

@permission_required('auth.agent')
def create_contact(r):
    if r.method == 'POST':
        form = ContactForm(r.POST)
        if form.is_valid():
            form.save(r.user.profile)
    form = ContactForm()
    return render(r, 'sales/create_contact.html', context={'form': form})

@permission_required('auth.agent')
def update_contact(r, id):
    if r.method == 'POST':
        form = ContactForm(r.POST, instance=Contact.objects.get(pk=id))
        if form.is_valid():
            form.save()
    form = ContactForm(instance=Contact.objects.get(pk=id))
    return render(r, 'sales/update_contact.html', context={'form': form})

@permission_required('auth.agent')
def contact_details(r,id):
    contact = Contact.objects.get(pk=id)
    if r.method == "POST":
        form = InteractionForm(r.POST)
        if form.is_valid():
            form.save(agent=r.user, contact=contact)
            contact.next_contact_date = form.cleaned_data["date"]
            contact.save()
    return render(r, 'sales/contact_details.html', context={
        'сontact': contact,
        'form': InteractionForm(),
        'interactions': Interaction.objects.filter(contact_id=id),
    })

@permission_required('auth.superagent')
def delegate_list(r):
    if r.method == 'POST':
        c_ids = r.POST["cids"].split(",")
        agent_id = r.POST["agent"]
        if c_ids[0] is not '':
            Contact.objects.filter(id__in=c_ids).update(agent=Profile.objects.get(pk=agent_id))

    contacts = Contact.objects.filter(in_sales=True)
    page = r.GET.get('page', 1)
    num = r.GET.get('num', 50)
    paginator = Paginator(contacts, num)
    try:
        contacts_paginated = paginator.page(page)
    except PageNotAnInteger:
        contacts_paginated = paginator.page(1)
    except EmptyPage:
        contacts_paginated = paginator.page(paginator.num_pages)
    return render(r, 'sales/delegate_list.html', context={'contact_list': contacts_paginated, 'agent_form':AgentForm()})

@permission_required('auth.admin')
def manage_list(r):
    if r.method == 'POST' and "file" in r.FILES:
        lines = [l.decode("utf-8") for l in r.FILES["file"].readlines()]
        source = r.POST['source']
        reader = csv.reader(lines)
        contacts = []
        next(reader)
        for c in reader:
            contacts.append(Contact(
                phone_main=c[0],
                first_name=c[1],
                last_name=c[2],
                source=source
            ))
        Contact.objects.bulk_create(contacts)
        
        return render(r, 'sales/manage_list.html')
    elif r.method == 'POST' and "cids" in r.POST:
        c_ids = r.POST["cids"].split(",")
        if c_ids[0] is not '':
            Contact.objects.filter(id__in=c_ids).update(in_sales=True)
    contacts = Contact.objects.all()
    page = r.GET.get('page', 1)
    num = r.GET.get('num', 50)

    paginator = Paginator(contacts, num)
    try:
        contacts_paginated = paginator.page(page)
    except PageNotAnInteger:
        contacts_paginated = paginator.page(1)
    except EmptyPage:
        contacts_paginated = paginator.page(paginator.num_pages)
    return render(r, 'sales/manage_list.html', context={'contact_list': contacts_paginated})

