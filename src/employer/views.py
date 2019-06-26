from django.shortcuts import render
from .forms import *
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect


class CreateVacancy(TemplateView):
    form = VacancyForm
    template_name = 'vacancy_form.html'

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, context={'form': form})

