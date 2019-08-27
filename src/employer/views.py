from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect

from .forms import *
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.http import HttpResponseRedirect


def perm(permission=''):
    class PermissionMixin(PermissionRequiredMixin):
        permission_required = permission

        def handle_no_permission(self):
            return redirect('/')
    return PermissionMixin


class CreateVacancy(perm('auth.director'), TemplateView):
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


class CreateEmployer(perm('auth.director'), CreateView):
    template_name = 'create_employer_form.html'
    form_class = CreateEmployerForm
    success_url = "/"


class EmployerDetail(perm('auth.director'), DetailView):
    model = Employer
    slug_field = 'id'


class EmployerList(perm('auth.director'), ListView):
    model = Employer


class VacancyList(perm('auth.agent'), ListView):
    model = Vacancy

    def get_queryset(self):
        queryset = Vacancy.objects.all()
        if "id" in self.kwargs:
            queryset = Vacancy.objects.filter(employer__pk=self.kwargs["id"])
        return queryset

class CreateContactPerson(perm('auth.director'), TemplateView):
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

class CreateExpense(perm('auth.director'),TemplateView):
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


@permission_required('auth.director')
def expenses_list(request):
    expenses = Expenses.objects.all()
    return render(request, 'expenses_list.html', context={'expenses': expenses})


@permission_required('auth.director')
def vacancy_create_note(request):
    if request.method == 'POST':
        note_form = CreateNoteForm(request.POST)
        if note_form.is_valid():
            note = note_form.save()
            note.save()
        return redirect(request, 'vacancy_note.html', pk=note.pk)


@permission_required('auth.director')
def employer_create_note(request):
    if request.method == 'POST':
        note_form = CreateNoteForm(request.POST)
        if note_form.is_valid():
            note = note_form.save()
            note.save()
        return redirect(request, 'employer_note.html', pk=note.pk)


@permission_required('auth.superagent')
def agent_create_note(request):
    if request.method == 'POST':
        note_form = CreateNoteForm(request.POST)
        if note_form.is_valid():
            note = note_form.save()
            note.save()
        return redirect(request, 'agent_note.html', pk=note.pk)


@permission_required('auth.agent')
def vacancy_detail(r, id):
    vacancy = Vacancy.objects.get(pk=id)
    return render(r, 'employer/vacancy_detail.html', context={'v': vacancy})
