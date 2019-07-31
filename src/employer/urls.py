from django.urls import path
from .views import *


app_name = "employer"
urlpatterns = [
    path("<id>/vacancy/create", CreateVacancy.as_view(), name="vacancy_create"),
    path("<id>/vacancy/", VacancyList.as_view(), name="vacancy_list"),

    path("", EmployerList.as_view(), name="employers_list"),
    path("create/", CreateEmployer.as_view(), name="employer_create"),
    path("<id>/vacancy", EmployerList.as_view(), name="employers_vacancy_list"),
    path("<id>/contacts/", CreateContactPerson.as_view(), name="employer_contact_create"),
    path("<id>/contacts/<contact_id>/", ContactPersonDetail.as_view(), name="employer_contact_detail"),
    path("<id>/contacts/", contact_persons_list, name="employer_contacts"),
    path("<pk>/", EmployerDetail.as_view(), name="employer_detail"),
    path("create_expense/", CreateExpense.as_view(), name="create_expense"),
    path("expenses_list/", expenses_list, name="expenses_list"),
]

