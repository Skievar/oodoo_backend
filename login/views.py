from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from login.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
