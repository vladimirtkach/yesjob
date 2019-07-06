from django.urls import path
from .views import *

urlpatterns = [
    path("vacancy/", CreateVacancy.as_view(), name="vacancy_url"),
    path("create_employer/", CreateEmployer.as_view(), name="create_employer_url"),
    path("employer_detail/", EmployerDetail.as_view(), name="employer_detail_url"),
    path("employers_list/", employers_list, name="employers_list_url"),
]
