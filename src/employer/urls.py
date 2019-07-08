from django.urls import path
from .views import *

urlpatterns = [
    path("vacancy/", CreateVacancy.as_view(), name="vacancy_url"),
    path("create_employer/", CreateEmployer.as_view(), name="create_employer_url"),
    path("employer/<slug>/", EmployerDetail.as_view(), name="employer_detail_url"),
    path("employers_list/", employers_list, name="employers_list_url"),
    path("create_contact_person/", CreateContactPerson.as_view(), name="create_contact_person_url"),
    path("contact_person/<slug>/", ContactPersonDetail.as_view(), name="contact_person_detail_url"),
    path("contact_persons_list/", contact_persons_list, name="contact_persons_list_url"),
    path("create_contact_languages/", CreateContactLanguages.as_view(), name='create_contact_languages'),
    path("contact_languages/<slug>/", ContactLanguagesDetail.as_view(), name='contact_languages_detail_url'),
    path("contact_languages_list/", contact_languages_list, name='contact_languages_list_url'),
]
