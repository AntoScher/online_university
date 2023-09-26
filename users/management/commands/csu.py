from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Admin
        user = User.objects.create(
            email='svetars2015@yandex.ru',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password('123genshin456')
        user.save()

        # User_1
        user = User.objects.create(
            email='anna@mail.ru',

        )
        user.set_password('111test222')
        user.save()

        # User_2

        user = User.objects.create(
            email='dmitry@mail.ru',

        )
        user.set_password('666test666')
        user.save()

        # User_3

        user = User.objects.create(
            email='maxim@tmail.ru',

        )
        user.set_password('333test333')
        user.save()
