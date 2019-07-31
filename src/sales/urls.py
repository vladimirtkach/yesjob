from django.urls import path
from django.conf.urls import url
from .views import *


from . import views

app_name = "sales"
urlpatterns = [
    path("contact_list", contact_list, name="contact_list"),
    path("create_contact", create_contact, name="create_contact"),
]
