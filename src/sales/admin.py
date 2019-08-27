from django.contrib import admin
from .models import *



@admin.register(Contact, SkillProfile, ContactSource)
class ContactAdmin(admin.ModelAdmin):
    pass
