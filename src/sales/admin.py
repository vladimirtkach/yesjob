from django.contrib import admin
from .models import *



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
