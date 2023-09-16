from django.urls import path
from education.apps import EducationConfig
from rest_framework.routers import DefaultRouter
from education.views import CourseViewSet, SubscriptionViewSet
from education.views import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, LessonDestroyAPIView
from education.views import PaymentListAPIView

app_name = EducationConfig.name

router = DefaultRouter()
# COURSE
router.register(r'courses', CourseViewSet, basename='courses')
# SUBSCRIPTION
router.register(r'subscriptions', SubscriptionViewSet, basename='subscriptions')

urlpatterns = [
    # LESSON
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_one'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
    # PAYMENT
    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),


] + router.urls
