from django.shortcuts import render
from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from education.models import Course, Lesson, Payment
from education.serializers import CourseSerializer, LessonSerializer, PaymentSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny

from education.permissions import CustomPermission


class MixinQueryset:
    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user.pk)
        return queryset



'''COURSE ViewSets'''
# ----------------------------------------------------------------


class CourseViewSet(MixinQueryset, viewsets.ModelViewSet):
    '''ViewSet Course'''
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [CustomPermission]

    def perform_create(self, serializer):
        new_course = serializer.save(owner=self.request.user)
        new_course.owner = self.request.user
        new_course.save()


'''LESSON generics'''
# ----------------------------------------------------------------


class LessonCreateAPIView(generics.CreateAPIView):
    '''CREATE Lesson'''
    serializer_class = LessonSerializer
    permission_classes = [CustomPermission]

    def perform_create(self, serializer):
        new_lesson = serializer.save(owner=self.request.user)
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(MixinQueryset, generics.ListAPIView):
    '''READ ALL Lesson'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()



class LessonRetrieveAPIView(MixinQueryset, generics.RetrieveAPIView):
    '''READ ONE Lesson'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(MixinQueryset, generics.UpdateAPIView):
    '''UPDATE PUT AND PATCH Lesson'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    '''DELETE Lesson'''
    queryset = Lesson.objects.all()
    permission_classes = [CustomPermission]


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
