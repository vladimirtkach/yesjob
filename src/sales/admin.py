from django.contrib import admin
from .models import *



@admin.register(Contact, SkillProfile, ContactSource, Objection)
class ContactAdmin(admin.ModelAdmin):
    pass
