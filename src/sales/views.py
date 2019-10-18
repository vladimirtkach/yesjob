from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from .filters import ContactFilter
from .models import *
from .forms import *
import csv
# Create your views here.

User = get_user_model()

status_colors = {
    -2: "red",
    -1: "orange",
    0: "",
    1: "yellow",
    2: "skyblue",
    3: "green",
    4: "blue",
}


def get_or (l, idx, default=""):
  try:
    return l[idx]
  except IndexError:
    return default



@permission_required('auth.agent')
def contact_list(r):
    # contacts=None
    # order = r.GET.get("order", "next_contact_date")
    # if r.method=='POST' and "search" in r.POST:
    #     if r.POST["search_type"] == "tel1":
    #         contacts = Contact.objects.filter(agent=r.user.profile, in_sales=True, phone_main__contains=r.POST["search"]).order_by(order)
    #     if r.POST["search_type"] == "tel2":
    #         contacts = Contact.objects.filter(agent=r.user.profile, in_sales=True, phone_secondary__contains=r.POST["search"]).order_by(order)
    #     if r.POST["search_type"] == "last_name":
    #         contacts = Contact.objects.filter(agent=r.user.profile, in_sales=True, last_name__contains=r.POST["search"]).order_by(order)
    # else:
    #     contacts = Contact.objects.filter(agent=r.user.profile, in_sales=True).order_by(order)


    page = r.GET.get('page', 1)
    num = r.GET.get('num', 50)
    contacts = ContactFilter(r.GET, queryset=Contact.objects.filter(agent=r.user.profile, in_sales=True))
    paginator = Paginator(contacts.qs, num)
    try:
        contacts_paginated = paginator.page(page)
    except PageNotAnInteger:
        contacts_paginated = paginator.page(1)
    except EmptyPage:
        contacts_paginated = paginator.page(paginator.num_pages)
    return render(r, 'sales/contact_list.html', context=
    {'contact_list': contacts_paginated, 'filter': contacts, 'request':r,
     'order': "next_contact_date"})

@permission_required('auth.agent')
def create_contact(r):
    form = ContactForm()
    if r.method == 'POST':
        form = ContactForm(r.POST)
        if form.is_valid():
            form.instance.color = status_colors[form.instance.lead_quality]
            instance = form.save(r.user.profile)
            return HttpResponseRedirect(reverse('sales:interactions', args=[instance.id]))
    return render(r, 'sales/create_contact.html', context={'form': form})

@permission_required('auth.agent')
def update_contact(r, id):
    form = ContactForm(instance=Contact.objects.get(pk=id))
    if r.method == 'POST':
        form = ContactForm(r.POST, instance=Contact.objects.get(pk=id))
        if form.is_valid():
            form.instance.color = status_colors[form.instance.lead_quality]
            form.save(r.user.profile)
            return HttpResponseRedirect(reverse('sales:interactions', args=[id]))
    return render(r, 'sales/update_contact.html', context={'form': form})

@permission_required('auth.agent')
def interactions(r,id):
    contact = Contact.objects.get(pk=id)
    if r.method == "POST":
        form = InteractionForm(r.POST)
        if form.is_valid():
            interaction = form.save(agent=r.user, contact=contact)
            contact.next_contact_date = form.cleaned_data["date"]
            contact.last_contact_date = datetime.now()
            contact.save()
            if r.POST["vac_id"] != "nosale":#nosale is default value for no sale))
                vac_id=r.POST["vac_id"]
                vacancy = Vacancy.objects.get(pk=vac_id)
                order = Order(sale_agent=r.user, provision_agent=r.user, interaction=interaction, contact=contact, vacancy=vacancy)
                order.save()

    positions = Vacancy.objects.filter(status="active")
    return render(r, 'sales/interactions.html', context={
        'сontact': contact,
        'positions': positions,
        'form': InteractionForm(),
        'interactions': Interaction.objects.filter(contact_id=id),
    })

@permission_required('auth.superagent')
def delegate_list(request):
    if request.method == 'POST' and "cids" in request.POST:
        c_ids = request.POST["cids"].split(",")
        agent_id = request.POST["agent"]
        if c_ids[0] is not '':
            Contact.objects.filter(id__in=c_ids).update(agent=Profile.objects.get(pk=agent_id))

    contacts = None
    if request.method == 'POST' and "search" in request.POST:
        contacts = Contact.objects.filter(phone_main__contains=request.POST["search"])
    elif "agent" in request.GET:
        contacts = Contact.objects.filter(in_sales=True, agent_id=request.GET["agent"]).order_by("-id")
    else:
        contacts = Contact.objects.filter(in_sales=True).order_by("-id")
    page = request.GET.get('page', 1)
    num = request.GET.get('num', 200)
    paginator = Paginator(contacts, num)
    try:
        contacts_paginated = paginator.page(page)
    except PageNotAnInteger:
        contacts_paginated = paginator.page(1)
    except EmptyPage:
        contacts_paginated = paginator.page(paginator.num_pages)
    return render(request, 'sales/delegate_list.html', context={'contact_list': contacts_paginated, 'agent_form':AgentForm(), 'request':request})

@permission_required('auth.admin')
def manage_list(r):
    if r.method == 'POST' and "file" in r.FILES:
        lines = [l.decode("utf-8") for l in r.FILES["file"].readlines()]
        source = ContactSource.objects.get(pk=r.POST['source'])
        #reader = csv.reader(lines,  d="|||")
        reader = lines
        contacts = []
        for c in reader:
            line = c.split(";")
            contacts.append(Contact(
                phone_main=normalize_phone(get_or(line,0)),
                first_name=get_or(line,1),
                last_name=get_or(line,2),
                cv_url=get_or(line,3),
                cv_title=get_or(line,4),
                email=get_or(line,5),
                source=source,
                comment=get_or(line,6),
                age=get_or(line,7),
                city=get_or(line,8),

            ))
        Contact.objects.bulk_create(contacts, ignore_conflicts=True)

        # return render(r, 'sales/manage_list.html')
    elif r.method == 'POST' and "cids" in r.POST:
        c_ids = r.POST["cids"].split(",")
        if c_ids[0] is not '':
            Contact.objects.filter(id__in=c_ids).update(in_sales=True)
    contacts = Contact.objects.all()
    page = r.GET.get('page', 1)
    num = r.GET.get('num', 200)
    sources = ContactSource.objects.all()
    paginator = Paginator(contacts, num)
    try:
        contacts_paginated = paginator.page(page)
    except PageNotAnInteger:
        contacts_paginated = paginator.page(1)
    except EmptyPage:
        contacts_paginated = paginator.page(paginator.num_pages)
    return render(r, 'sales/manage_list.html', context={'contact_list': contacts_paginated, "sources":sources})


@permission_required('auth.agent')
def order_list(r):
    if r.user.groups.filter(name='Agent').exists():
        orders = orders = Order.objects.filter(sale_agent=r.user.id)
    else:
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


def postback_handle(r):
    ct_phone = r.GET.get("ct_phone")
    ct_button_num = r.GET.get("ct_button_num")
    if ct_button_num == "1":
        contact = Contact.objects.filter(phone_main__contains=ct_phone)
        interaction = Interaction(
            agent=User.objects.get(pk=1),
            contact=contact.first(),
            result="Успешный автопрозвон",
            type="автопрозвон"
        )
        interaction.save()

@permission_required('auth.agent')
def create_profile(r):
    form = SkillProfileForm()
    profiles = SkillProfile.objects.all()

    if r.method == 'POST':
        form = SkillProfileForm(r.POST)
        if form.is_valid():
            form.save()
    return render(r, 'sales/create_profile.html', context={'form': form, 'profiles': profiles})


class ContactSourceList(ListView):
    model = ContactSource


@permission_required('auth.superagent')
def create_contact_source(r):
    form = ContactSourceForm()

    if r.method == 'POST':
        form = ContactSourceForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('sales:contact_source_list'))
    return render(r, 'sales/create_contact_source.html', context={'form': form})


