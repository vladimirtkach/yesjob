from django.contrib import admin
from .models import *



@admin.register(Contact, SkillProfile)
class ContactAdmin(admin.ModelAdmin):
    pass
