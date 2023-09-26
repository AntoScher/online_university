import re
from rest_framework.validators import ValidationError


class YouTubeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        '''Проверяет отсутствие в материалах ссылок на сторонние ресурсы, кроме youtube.com'''
        reg = re.compile(r"https://youtube.com")
        video_field = dict(value).get(self.field)

        if not bool(reg.search(video_field)):
            raise ValidationError('Разрешаются только ссылки на YouTube')
