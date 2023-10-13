# Платформа для онлайн обучения.
<br>

## Цель проекта:

> Реализовать платформу для онлайн-обучения. 
Разработка LMS-системы, в которой каждый желающий может размещать свои полезные материалы или курсы.


### Настройка DRF в Docker

**Клонировать проект:**
> https://github.com/svro2022/DRF_homework.git

**Сборка докер образа:**
> docker build -t my-python-app .

**Запуск контейнера:**
> docker run my-python-app

<br>
<br>
<br>

### Базовые команды в PyCharm

Создание виртуального окружения:
> python -m venv venv

Активация виртуального окружения:
> source venv/bin/activate

Установка зависимостей:
> pip install -r requirements.txt

Миграции в БД
> python manage.py migrate

Создание администратора и нескольких пользователей:
> python3 manage.py csu

Запуск приложение JangoDRF:
> python manage.py runserver

Запуск Redis:
> redis-cli

Запуск Celery:
отложенные задачи
> celery -A config worker -l INFO

Запуск Celery-beat:
периодические задачи
> celery -A config beat -l INFO -s django

Запуск юниттестов:
> python3 manage.py test


По необходимости проверка работы PostgreSQL:
> service postgresql status

Зайти в Postgre от суперпользователя:
> psql -U postgres

Выход:
> exit