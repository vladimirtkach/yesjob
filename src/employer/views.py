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
    form = EmployerForm
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

    def get(self, request):
        employer = get_object_or_404(Employer)
        return render(request, self.template_name, context={'employer': employer})


def employers_list(request):
    employers_lst = Employer.objects.all()
    return render(request, 'employers_list.html', context={'employers_lst': employers_lst})
