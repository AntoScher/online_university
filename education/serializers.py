from rest_framework import serializers
from education.models import Course, Lesson, Payment, Subscription
from education.validators import YouTubeValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [YouTubeValidator(field='link_video')]


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

    def get_is_subscribed(self, obj):
        '''Проверка подписки на курс'''
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Subscription.objects.filter(user=request.user, course=obj).exists()
        return False


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'
