from django.contrib import admin
from .models import Employer, ContactPerson, Language, Expenses, Vacancy
from django.contrib.auth.models import Permission

admin.site.register(Permission)

@admin.register(Employer, ContactPerson, Language, Expenses, Vacancy)
class AuthorAdmin(admin.ModelAdmin):
    pass

