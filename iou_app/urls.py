from django.urls import path, include
from . import views
from graphene_django.views import GraphQLView
from .schema import schema
from rest_framework_swagger.views import get_swagger_view

swagger_schema_view = get_swagger_view(title='IOU App Rest API')

urlpatterns = [
    path('api/', views.restApiOverview, name='Rest-api-overview'),
    path('api/all-users/', views.listAllUsers, name='All users list'),
    path('api/user-detail/<str:pk>/', views.userDetail,
         name="Get a user's details"),
    path('api/create-iou/', views.createIOU, name="Create an IOU"),
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
    path('api-docs/',
         swagger_schema_view),
]
