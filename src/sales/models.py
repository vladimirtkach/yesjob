from django.db import models
from employer.models import Vacancy
from django.conf import settings


class Contact(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone_main = models.CharField(max_length=50, blank=True)
    phone_secondary = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(blank=True)
    contactable = models.BooleanField(default=False)
    is_pair = models.BooleanField(default=False)
    sex = models.BooleanField(default=False)
    is_lead = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    in_sales = models.BooleanField(default=False)
    profiles = models.ManyToManyField("SkillProfile")

    def __str__(self):
        return self.first_name


class Interaction(models.Model):
    agent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, blank=True)


class SkillProfile(models.Model):
    name = models.CharField(max_length=50, blank=True)



# class Order(models.Model):
#     vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
#     contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
#     interaction =


