from django.urls import path
from django.conf.urls import url
from .views import *


from . import views

app_name = "strategy"
urlpatterns = [
    path("status/", status, name="status"),

]
