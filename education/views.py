from django.shortcuts import render
from rest_framework import viewsets, generics
from education.models import Course, Lesson
from education.serializers import CourseSerializer, LessonSerializer


'''COURSE ViewSets'''
# ----------------------------------------------------------------


class CourseViewSet(viewsets.ModelViewSet):
    '''ViewSet Course'''
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


'''LESSON generics'''
# ----------------------------------------------------------------


class LessonCreateAPIView(generics.CreateAPIView):
    '''CREATE Lesson'''
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    '''READ ALL Lesson'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    '''READ ONE Lesson'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    '''UPDATE PUT AND PATCH Lesson'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    '''DELETE Lesson'''
    queryset = Lesson.objects.all()
