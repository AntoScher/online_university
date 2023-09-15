from django.shortcuts import render
from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from education.models import Course, Lesson, Payment
from education.serializers import CourseSerializer, LessonSerializer, PaymentSerializer

from rest_framework.permissions import IsAuthenticated
from education.permissions import IsStaff, IsOwnerOrStaff


'''COURSE ViewSets'''
# ----------------------------------------------------------------


class CourseViewSet(viewsets.ModelViewSet):
    '''ViewSet Course'''
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]


'''LESSON generics'''
# ----------------------------------------------------------------


class LessonCreateAPIView(generics.CreateAPIView):
    '''CREATE Lesson'''
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]


class LessonListAPIView(generics.ListAPIView):
    '''READ ALL Lesson'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    '''READ ONE Lesson'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsStaff]


class LessonUpdateAPIView(generics.UpdateAPIView):
    '''UPDATE PUT AND PATCH Lesson'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsStaff]


class LessonDestroyAPIView(generics.DestroyAPIView):
    '''DELETE Lesson'''
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]


'''PAYMENT generics'''
# ----------------------------------------------------------------


class PaymentListAPIView(generics.ListAPIView):
    '''READ ALL Payments, Добавлена фильтрация'''
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course', 'lesson', 'payment_method']
    ordering_fields = ['payment_date']
    permission_classes = [IsAuthenticated]
