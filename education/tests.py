from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from education.models import Course, Lesson, Subscription
from users.models import User


class EducationTestCase(APITestCase):
    '''Тест моделей Course и Lesson'''

    def setUp(self) -> None:
        '''Создается тестовый пользователь'''
        self.user = User.objects.create(
            email='test@mail.ru',
        )
        self.user.set_password('555test555')
        self.user.save()
        self.client.force_authenticate(user=self.user)

        '''Создается тестовый курс'''
        self.course = Course.objects.create(
            title='test course',
            description='test course description'
        )

        '''Создается тестовый урок'''
        self.lesson = Lesson.objects.create(
            title='test lesson',
            description='test lesson description',
            link_video='https://www.youtube.com/',
            course=self.course,
            owner=self.user
        )

    def test_create_lesson(self):
        '''Тест CREATE lesson'''

        url = reverse('education:lesson_create')

        data = {
            'title': 'test lesson2',
            'description': 'test lesson2 description',
            'link_video': 'https://www.youtube.com',
            'course': self.course.pk,
            'owner': self.user.pk
        }

        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_list_lesson(self):
        '''Тест READ LIST lesson'''
        url = reverse('education:lesson_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_retrieve_lesson(self):
        '''Тест READ ONE lesson'''
        url = reverse('education:lesson_one', kwargs={'pk': self.lesson.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.lesson.title)

    def test_update_lesson(self):
        '''Тест UPDATE lesson'''
        url = reverse('education:lesson_update', kwargs={'pk': self.lesson.pk})
        new_title = 'test_title'
        data = {'title': new_title}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, new_title)

    def test_delete_lesson(self):
        '''Тест DELETE lesson'''
        url = reverse('education:lesson_delete', kwargs={'pk': self.lesson.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.filter(pk=self.lesson.pk).exists())



class SubscriptionTestCase(APITestCase):
    '''Тест модели Subscription'''
    def setUp(self) -> None:
        '''Создается тестовый пользователь'''
        self.user = User.objects.create(
            email='test2@mail.ru',
        )
        self.user.set_password('777test777')
        self.user.save()
        self.client.force_authenticate(user=self.user)

        '''Создается тестовый курс'''
        self.course = Course.objects.create(
            title='test course for subscription',
            description='test course subscription'
        )

        self.data = {
            'user': self.user,
            'course': self.course,
        }

        self.subscription = Subscription.objects.create(**self.data)

    def test_create_subscription(self):
        '''Тест CREATE Subscription'''
        data = {
            'user': self.user.pk,
            'course': self.course.pk,
        }
        url = reverse('education:subscriptions')
        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        subscription = Subscription.objects.get(user=self.user, course=self.course)
        self.assertTrue(subscription.is_subscribe)

    def test_delete_subscription(self):
        '''Тест DELETE Subscription'''
        subscription = Subscription.objects.create(user=self.user, course=self.course, is_subscribe=True)
        url = reverse('education:subscriptions', kwargs={'pk': subscription.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Subscription.objects.filter(id=subscription.id).exists())
