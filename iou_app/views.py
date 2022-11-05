from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Users, Owes
from .serializers import UserSerializer, OwesSerializer, UserObjSerializer
# Create your views here.


@api_view(['GET'])
def restApiOverview(request):
    api_overview = {
        'List Debts': '/settleup',
        'Create User': '/add',
        'Create IOU': '/iou',
        'Graphql': '/expired_iou',
    }
    return Response(api_overview)


@api_view(['GET'])
def listAllUsers(request):
    all_users = Users.objects.all()
    serialized_users = UserSerializer(all_users, many=True)
    return Response(serialized_users.data)


@api_view(['GET'])
def userDetail(request, pk):
    user = Users.objects.get(id=pk)
    serialized_user = UserSerializer(user, many=False)
    return Response(serialized_user.data)


@api_view(['GET'])
def settleUp(request):
    userlist = request.query_params.getlist('users')
    userlist.sort()
    userObjList = []
    for user in userlist:
        userObjList.append(getUserObj(user))
    return Response(userObjList)


@api_view(['POST'])
def addUser(request):
    # serialized_iou = createIOUSerializer(request.data)
    user_added = Users.objects.create({'name': request.data['user']})
    return Response({
        'users': getUserObj(user_added['name'])
    })


@api_view(['POST'])
def createIOU(request):
    # serialized_iou = createIOUSerializer(request.data)
    iou_record = Owes.objects.create(request.data)
    userlist = [iou_record['lender'], iou_record['borrower']]
    userlist.sort()
    return Response({
        'users': [getUserObj(userlist[0]), getUserObj(userlist[1])]
    })


def getUserObj(user_name):
    owes_items = Owes.objects.filter(borrower=user_name).values()
    lent_items = Owes.objects.filter(lender=user_name).values()
    user_obj = UserObjSerializer({
        'user_name': user_name,
        'owes_items': owes_items,
        'lent_items': lent_items,
    })
    return user_obj
