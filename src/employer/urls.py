from django.urls import path
from .views import *

urlpatterns = [
    path("vacancy/create", CreateVacancy.as_view(), name="vacancy_create"),
    path("vacancy/", CreateVacancy.as_view(), name="vacancy_list"),

    path("employer/", EmployerList.as_view(), name="employers_list"),
    path("employer/create/", CreateEmployer.as_view(), name="employer_create"),
    path("employer/<id>/vacancy", EmployerList.as_view(), name="employers_vacancy_list"),
    path("employer/<id>/contacts/", CreateContactPerson.as_view(), name="employer_contact_create"),
    path("employer/<id>/contacts/<contact_id>/", ContactPersonDetail.as_view(), name="employer_contact_detail"),
    path("employer/<id>/contacts/", contact_persons_list, name="employer_contacts"),
    path("employer/<id>/", EmployerDetail.as_view(), name="employer_detail"),
]

