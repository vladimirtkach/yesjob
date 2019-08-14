from django.urls import path
from django.conf.urls import url
from .views import *
from . import views

app_name = "sales"
urlpatterns = [
    path("contact_list", contact_list, name="contact_list"),
    path("delegate_list", delegate_list, name="delegate_list"),
    path("create_contact", create_contact, name="create_contact"),
    path("update_contact/<id>", update_contact, name="update_contact"),
    path("contact_details/<id>", contact_details, name="contact_details"),
    path("manage_list", manage_list, name="manage_list"),
]
