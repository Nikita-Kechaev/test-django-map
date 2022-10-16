# test-django-map
* Тестовое задание для Fogstream
## Развертываение проекта:
* Скачать репоизиторий на локальную машину
* В корневой папке проекта создать файл .env (константы для заполнения в .env_example)
* В консоли перейти в корень проекта
* Выполнить команду sudo docker compose -f docker-compose.yaml up -d
* Для создания суперпользователя - sudo docker compose exec web bash python manage.py createsuperuser
