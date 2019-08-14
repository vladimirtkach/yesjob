from datetime import datetime

from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import date
from employer.models import Vacancy
from profiles.models import Profile
from django.conf import settings


class Contact(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone_main = models.CharField(max_length=50)
    phone_secondary = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(blank=True, default=0)
    sex = models.CharField(max_length=1, blank=True, choices=(("м", "Мужской"),("ж", "Женский")))
    is_client = models.BooleanField(default=False)
    in_sales = models.BooleanField(default=False)
    profiles = models.ManyToManyField("SkillProfile", default=None)
    agent = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    source = models.CharField(max_length=50)
    lead_quality = models.IntegerField(default=0)
    city = models.CharField(max_length=50, default='', blank=True)
    next_contact_date = models.DateTimeField( auto_now=True)
    comment = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.first_name

class SkillProfile(models.Model):
    name = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.name

class Interaction(models.Model):
    agent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    result = models.CharField(max_length=200, blank=True)
    interaction_date = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=200, choices=(("звонок", "Звонок"),("email", "Email"),("sms", "Sms"),("messenger", "Messenger")))


class Order(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    interaction = models.ForeignKey(Interaction, on_delete=models.CASCADE)
    sale_agent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sale_agent',  default=None)
    provision_agent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='provision_agent', default=None)
