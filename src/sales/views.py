from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import ListView

from .models import *
from .forms import *
import csv
# Create your views here.

User = get_user_model()


class ContactSourceList(ListView):
    model = ContactSource


@permission_required('auth.agent')
def contact_list(r):
    contacts=None
    order = r.GET.get("order", "next_contact_date")
    if r.method=='POST' and "search" in r.POST:
        if r.POST["search_type"] == "tel1":
            contacts = Contact.objects.filter(agent=r.user.profile, in_sales=True, phone_main__contains=r.POST["search"]).order_by(order)
        if r.POST["search_type"] == "tel2":
            contacts = Contact.objects.filter(agent=r.user.profile, in_sales=True, phone_secondary__contains=r.POST["search"]).order_by(order)
        if r.POST["search_type"] == "last_name":
            contacts = Contact.objects.filter(agent=r.user.profile, in_sales=True, last_name__contains=r.POST["search"]).order_by(order)
    else:
        contacts = Contact.objects.filter(agent=r.user.profile, in_sales=True).order_by(order)
    page = r.GET.get('page', 1)
    num = r.GET.get('num', 50)

    paginator = Paginator(contacts, num)
    try:
        contacts_paginated = paginator.page(page)
    except PageNotAnInteger:
        contacts_paginated = paginator.page(1)
    except EmptyPage:
        contacts_paginated = paginator.page(paginator.num_pages)
    return render(r, 'sales/contact_list.html', context=
    {'contact_list': contacts_paginated,
     'order': order})

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
            interaction = form.save(agent=r.user, contact=contact)
            contact.next_contact_date = form.cleaned_data["date"]
            contact.save()
            if r.POST["vac_id"] != "nosale":
                vac_id=r.POST["vac_id"]
                vacancy = Vacancy.objects.get(pk=vac_id)
                order = Order(sale_agent=r.user, provision_agent=r.user, interaction=interaction, contact=contact, vacancy=vacancy)
                order.save()

    positions = Vacancy.objects.filter(status="active")
    return render(r, 'sales/contact_details.html', context={
        'сontact': contact,
        'positions': positions,
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

    contacts = None
    if "agent" in r.GET:
        contacts = Contact.objects.filter(in_sales=True, agent_id=r.GET["agent"])
    else:
        contacts = Contact.objects.filter(in_sales=True)
    page = r.GET.get('page', 1)
    num = r.GET.get('num', 200)
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
        source = ContactSource.objects.get(pk=r.POST['source'])
        reader = csv.reader(lines)
        contacts = []
        next(reader)
        for c in reader:
            contacts.append(Contact(
                phone_main=c[0],
                first_name=c[1],
                last_name=c[2],
                cv_url=c[3],
                email=c[4],
                source=source,
                in_sales=True,
            ))
        Contact.objects.bulk_create(contacts, ignore_conflicts=True)
        
        return render(r, 'sales/manage_list.html')
    elif r.method == 'POST' and "cids" in r.POST:
        c_ids = r.POST["cids"].split(",")
        if c_ids[0] is not '':
            Contact.objects.filter(id__in=c_ids).update(in_sales=True)
    contacts = Contact.objects.all()
    page = r.GET.get('page', 1)
    num = r.GET.get('num', 200)

    paginator = Paginator(contacts, num)
    try:
        contacts_paginated = paginator.page(page)
    except PageNotAnInteger:
        contacts_paginated = paginator.page(1)
    except EmptyPage:
        contacts_paginated = paginator.page(paginator.num_pages)
    return render(r, 'sales/manage_list.html', context={'contact_list': contacts_paginated, "source_form":ContactSourceForm()})


@permission_required('auth.superagent')
def order_list(r):
    orders = Order.objects.all()
    page = r.GET.get('page', 1)
    num = r.GET.get('num', 50)

    paginator = Paginator(orders, num)
    try:
        orders_paginated = paginator.page(page)
    except PageNotAnInteger:
        orders_paginated = paginator.page(1)
    except EmptyPage:
        orders_paginated = paginator.page(paginator.num_pages)
    return render(r, 'sales/order_list.html', context={'orders': orders_paginated})

@permission_required('auth.superagent')
def agent_stats(r):
    agent_id = r.GET.get("agent", "all")
    start_date = r.GET.get("start_date", "2019-08-20")
    end_date = r.GET.get("end_date", "2019-08-31")

    interactions = None
    if agent_id == "all":
        interactions = Interaction.objects.filter(interaction_date__range=(start_date, end_date))
    else:
        interactions = Interaction.objects.filter(agent_id=agent_id, interaction_date__range=(start_date, end_date))
    orders_count = interactions.filter(order__isnull=False).count()
    form = AgentStats() if agent_id=="all" else AgentStats(r.GET)
    agent = "Все агенты" if agent_id=="all" else User.objects.get(pk=agent_id)
    return render(r, 'sales/agent_stats.html', context=
    {'orders_count': orders_count,'interactions': interactions, 'agent_stats_form': form, "agent":agent})
