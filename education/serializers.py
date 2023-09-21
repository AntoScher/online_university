from rest_framework import serializers
from education.models import Course, Lesson, Payment, Subscription
from education.validators import YouTubeValidator
from education.services import create_payment, retrieve_payment


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        #validators = [YouTubeValidator(field='link_video')]


class PaymentSerializer(serializers.ModelSerializer):
    payment = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = '__all__'

    def get_payment_stripe(self, instance):
        if self.request.stream.method == 'POST':
            stripe_id = create_payment(int(instance.payment_amount))
            obj_payments = Payment.objects.get(id=instance.id)
            obj_payments.stripe_id = stripe_id
            obj_payments.save()
            return retrieve_payment(stripe_id)
        if self.request.stream.method == 'GET':
            if not instance.stripe_id:
                return None
            return retrieve_payment(instance.stripe_id)


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
