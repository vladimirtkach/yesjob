from django.urls import path
from .views import *

urlpatterns = [
    path("vacancy/", CreateVacancy.as_view(), name="vacancy_url"),
]
