from django.contrib import admin
from .models import Employer, ContactPerson, Language


@admin.register(Employer)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactPerson)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Language)
class AuthorAdmin(admin.ModelAdmin):
    pass
