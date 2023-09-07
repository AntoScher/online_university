from django.db import models

# Constant
NULLABLE = {'blank': True, 'null': True}


# Course

class Course(models.Model):
    '''Курс'''
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
    title = models.CharField(max_length=200, verbose_name='Название')
    preview = models.ImageField(**NULLABLE, verbose_name='Превью')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    link_video = models.CharField(**NULLABLE, max_length=200, verbose_name='Ссылка на видео')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ('title',)
