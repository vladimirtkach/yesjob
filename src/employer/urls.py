from django.urls import path
from .views import *

urlpatterns = [
    path("vacancy/", CreateVacancy.as_view(), name="vacancy_url"),
    path("create/", CreateEmployer.as_view(), name="create_employer_url"),

    path("all/", EmployerList.as_view(), name="employers_list_url"),
    path("contacts/", CreateContactPerson.as_view(), name="create_contact_person_url"),
    path("contacts/<id>/", ContactPersonDetail.as_view(), name="contact_person_detail_url"),
    path("<id>/contacts/", contact_persons_list, name="contact_persons_list_url"),
    path("<id>/", EmployerDetail.as_view(), name="employer_detail_url"),
]

