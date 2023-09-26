from rest_framework import serializers
from education.serializers import PaymentSerializer

from users.models import User

from django import forms


class UserSerializer(serializers.ModelSerializer):
    '''Расширение сериализатора для вывода истории платежей user'''
    payments = PaymentSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        '''Скрыть пароль в профиле'''
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class UserLimitedSerializer(serializers.ModelSerializer):
    '''Исключает отображение пароля и фамилии'''
    class Meta:
        model = User
        exclude = ('password', 'last_name')
