from django.shortcuts import render
from rest_framework import viewsets
from education.models import Course
from education.serializers import CourseSerializer


'''COURSE'''
class CourseViewSet(viewsets.ModelViewSet):
    '''вьюсет Курса'''
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


'''LESSON'''
