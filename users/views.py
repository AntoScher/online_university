from django.shortcuts import render
from rest_framework import viewsets, generics
from users.models import User
from users.serializers import UserSerializer, UserLimitedSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import UserPermission


'''USER generics'''
# ----------------------------------------------------------------


class UserCreateAPIView(generics.CreateAPIView):
    '''CREATE User'''
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserListAPIView(generics.ListAPIView):
    '''READ ALL User'''
    serializer_class = UserLimitedSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    '''READ ONE User'''
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, UserPermission]


class UserUpdateAPIView(generics.UpdateAPIView):
    '''UPDATE PUT AND PATCH User'''
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, UserPermission]


class UserDestroyAPIView(generics.DestroyAPIView):
    '''DELETE User'''
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, UserPermission]
