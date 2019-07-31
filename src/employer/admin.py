from django.contrib import admin
from .models import Employer, ContactPerson, Language, Expenses, Vacancy


@admin.register(Employer, ContactPerson, Language, Expenses, Vacancy)
class AuthorAdmin(admin.ModelAdmin):
    pass

