from django.urls import path
from .views import *


app_name = "employer"
urlpatterns = [
    path("<id>/vacancy/create", CreateVacancy.as_view(), name="vacancy_create"),
    path("<id>/vacancy/", VacancyList.as_view(), name="vacancy_list"),
    path("vacancy/", VacancyList.as_view(), name="all_vacancies"),
    path("vacancy/<id>", vacancy_detail, name="vacancy_detail"),
    path("", EmployerList.as_view(), name="employers_list"),
    path("create/", CreateEmployer.as_view(), name="employer_create"),
    path("<id>/contacts/", CreateContactPerson.as_view(), name="employer_contact_create"),
    path("<pk>/", EmployerDetail.as_view(), name="employer_detail"),
    path("create_expense/", CreateExpense.as_view(), name="create_expense"),
    path("expenses_list/", expenses_list, name="expenses_list"),
    path("create_note/employer/", employer_create_note, name='employer_create_note'),
    path("create_note/vacancy/", employer_create_note, name='vacancy_create_note'),
    path("create_note/agent/", employer_create_note, name='agent_create_note'),
]


