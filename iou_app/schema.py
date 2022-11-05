import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Owes
from django.utils import timezone


class IOUType(DjangoObjectType):
    class Meta:
        model = Owes
        fields = (
            "id",
            "borrower",
            "lender",
            "amount",
            "expiration",
            "creation_time"
        )


class Query(graphene.ObjectType):
    current = timezone.now()

    all_expired_ious = DjangoListField(IOUType)

    def resolve_all_expired_ious(root, info):
        return Owes.objects.filter(expiration__lt=current)


schema = graphene.Schema(query=Query)
