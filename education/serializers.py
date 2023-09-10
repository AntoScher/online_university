from rest_framework import serializers
from education.models import Course, Lesson, Payment


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    '''Для сериализатора модели Course реализуем поле вывода уроков - lesson'''
    lesson_count = serializers.IntegerField(source='lessons.all.count',  read_only=True)
    lesson = LessonSerializer(source='lessons', many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['title', 'preview', 'description', 'lesson_count', 'lesson']

    @staticmethod
    def get_lesson_count(instanse):
        return instanse.lesson.count()
