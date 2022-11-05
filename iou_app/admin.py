from django.contrib import admin
from . import models


@admin.register(models.Users)
class UsersAdmin(admin.ModelAdmin):
    fields = [
        'id',
        'name',
    ]


@admin.register(models.Owes)
class OwesAdmin(admin.ModelAdmin):
    fields = [
        'id',
        'borrower',
        'lender',
        'amount',
        'expiration',
        'creation_time',
    ]
