from django.core.management import BaseCommand

from education.models import Payment
from users.models import User


class Command(BaseCommand):
    '''Создание платежа Payment'''

    def handle(self, *args, **options):
        user = User.objects.get(email='student482skypro@rambler.ru')

        Payment.objects.create(user=user, payment_date='2023-09-30',
                               course_id=2, lesson_id=2,
                               payment='10000', payment_method='cash')
