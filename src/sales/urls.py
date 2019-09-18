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
    path("interactions/<id>", interactions, name="interactions"),
    path("manage_list", manage_list, name="manage_list"),
    path("order_list", order_list, name="order_list"),
    path("agent_stats", agent_stats, name="agent_stats"),
    path("contact_source_list", ContactSourceList.as_view(), name="contact_source_list"),
    path("create_contact_source", create_contact_source, name="create_contact_source"),
    path("postback", postback_handle, name="postback_handle"),
    path("create_profile", create_profile, name="create_profile"),
]
