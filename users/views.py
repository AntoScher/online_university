from django.shortcuts import render
from rest_framework import viewsets, generics
from users.models import User
from users.serializers import UserSerializer


'''USER generics'''
# ----------------------------------------------------------------


class UserCreateAPIView(generics.CreateAPIView):
    '''CREATE User'''
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    '''READ ALL User'''
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    '''READ ONE User'''
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    '''UPDATE PUT AND PATCH User'''
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    '''DELETE User'''
    queryset = User.objects.all()

