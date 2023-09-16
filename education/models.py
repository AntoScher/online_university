from django.db import models
from users.models import User
from django.utils import timezone
from django.conf import settings

# Constants
NULLABLE = {'blank': True, 'null': True}

PAYMENT_METHOD = (
   ('cash', 'Наличные'),
   ('transfer', 'Перевод на счет'),
)


# Course

class Course(models.Model):
    '''Курс'''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    title = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(**NULLABLE, verbose_name='Превью')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ('title',)


# Lesson

class Lesson(models.Model):
    '''Урок'''
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', related_name='lessons', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    title = models.CharField(max_length=200, verbose_name='Название')
    preview = models.ImageField(**NULLABLE, verbose_name='Превью')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    link_video = models.CharField(**NULLABLE, max_length=200, verbose_name='Ссылка на видео')

    def __str__(self):
        return f'{self.title}{self.course}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ('title',)


# Payment

class Payment(models.Model):
    '''Платежи'''
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='payments', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)

    payment_date = models.DateField(default=timezone.now, verbose_name='Дата оплаты')
    payment_amount = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=15, choices=PAYMENT_METHOD, verbose_name='Способ оплаты')

    def __str__(self):
        return f'{self.user} - {self.payment_date} - {self.payment_amount}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'


# Subscription

class Subscription(models.Model):
    '''Подписки'''
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Подписка на курс', related_name='subscribe', **NULLABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Подписчик', **NULLABLE)

    is_subscribe = models.BooleanField(default=False, verbose_name="Подписка")

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
