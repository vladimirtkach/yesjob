from django.shortcuts import render, get_object_or_404
from .forms import *
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect


class CreateVacancy(TemplateView):
    form = VacancyForm
    template_name = 'create_vacancy_form.html'

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, context={'form': form})


class CreateEmployer(TemplateView):
    form = CreateEmployerForm
    template_name = 'create_employer_form.html'

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, context={'form': form})


class EmployerDetail(TemplateView):
    template_name = 'employer_detail.html'

    def get(self, request, id):
        employer = get_object_or_404(Employer, pk=id)
        return render(request, self.template_name, context={'employer': employer})


class EmployerList(TemplateView):
    template_name = 'employers_list.html'

    def get(self, request):
        employers_lst = Employer.objects.all()
        return render(request, 'employers_list.html', context={'employers_lst': employers_lst})




class CreateContactPerson(TemplateView):
    form = CreateContactPersonForm
    template_name = 'create_contact_person_form.html'

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
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





class ContactLanguagesDetail(TemplateView):
    template_name = 'contact_languages_detail.html'

    def get(self, request, slug):
        contact_languages = get_object_or_404(ContactLanguages, slug__iexact=slug)
        return render(request, self.template_name, context={'contact_languages': contact_languages})



