from rest_framework import serializers
from .models import Users, Owes
from .dataTransforms import getItemDetails, getUserObj


class OwesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owes
        fields = (
            'id',
            'borrower',
            'lender',
            'amount',
            'expiration',
            'creation_time',
        )
        depth = 1


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = (
            'id',
            'name'
        )


class UserObjSerializer(serializers.ModelSerializer):
    user_name = serializers.Field(source='user_name')
    owes_items = serializers.Field(source='owes_items')
    lent_items = serializers.Field(source='lent_items')
    user_obj = getUserObj(user_name, owes_items, lent_items)

    class Meta:
        fields = (
            'user_obj.name',
            'user_obj.owes',
            'user_obj.owed_by',
            'user_obj.balance',
        )
