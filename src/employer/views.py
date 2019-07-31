from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import *
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.http import HttpResponseRedirect


class CreateVacancy(LoginRequiredMixin, TemplateView):
    form = VacancyForm
    template_name = 'create_vacancy_form.html'

    def get(self, request, id):
        form = self.form()
        form.fields["employer"].initial = id
        return render(request, self.template_name, context={'form': form})

    def post(self, request, id):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employer/')
        return render(request, self.template_name, context={'form': form})


class CreateEmployer(LoginRequiredMixin, CreateView):
    template_name = 'create_employer_form.html'
    form_class = CreateEmployerForm
    success_url = "/"

class AdminRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        try:
            request.user.groups.get(name='vacancy')
            return super().dispatch(request, *args, **kwargs)
        except:
            return self.handle_no_permission()


def perm(permission=''):
    class PermissionMixin(PermissionRequiredMixin):
        permission_required = permission

        def handle_no_permission(self):
            return redirect('/')

    return PermissionMixin


class EmployerDetail(perm('employer.add_vacancy'), DetailView):
    model = Employer
    slug_field = 'id'


class EmployerList(LoginRequiredMixin, ListView):
    model = Employer


class VacancyList(ListView):
    model = Vacancy


class CreateContactPerson(LoginRequiredMixin, TemplateView):
    form = CreateContactPersonForm
    template_name = 'create_contact_person_form.html'

    def get(self, request, id):
        form = self.form()
        return render(request, self.template_name, context={'form': form})

    def post(self, request, id):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, context={'form': form})


def contact_persons_list(request, id):
    contact_persons = ContactPerson.objects.filter(employer__pk=id)
    return render(request, 'contact_persons_list.html', context={'contact_persons': contact_persons})


class ContactPersonDetail(TemplateView):
    template_name = 'contact_person_detail.html'

    def get(self, request, id):
        contact_person = ContactPerson.objects.get(pk=id)
        return render(request, self.template_name, context={'contact_person': contact_person})


class CreateExpense(TemplateView):
    form = CreateExpenseForm
    template_name = 'create_expense.html'

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, context={'form': form})


def expenses_list(request):
    expenses = Expenses.objects.all()
    return render(request, 'expenses_list.html', context={'expenses': expenses})



