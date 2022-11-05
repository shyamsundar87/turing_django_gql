# from typing_extensions import Required
from django.db import models
import uuid

from django.utils import timezone

# Create your models here.


class Users(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Owes(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)
    borrower = models.ForeignKey(
        Users, related_name='UserWhoOwes', blank=False, on_delete=models.DO_NOTHING, verbose_name=("Person with debt"))
    lender = models.ForeignKey(
        Users, related_name='UserHeOwesTo', blank=False, on_delete=models.DO_NOTHING, verbose_name=("Person indebted to"))
    amount = models.FloatField(
        blank=False, verbose_name=("Amount Indebted/Owed"))
    expiration = models.DateTimeField(
        blank=False, verbose_name=("Time of Expiration"))
    creation_time = models.DateTimeField(
        default=timezone.now, verbose_name=("Time of debt"))

    def __str__(self):
        return f'{self.borrower}_owes_to_{self.lender}'
