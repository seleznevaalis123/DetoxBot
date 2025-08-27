# Botwithapp
tg bot Django/nginx/PostgreSQL

# Django Project setup (macOS)

git clone <URL_репозитория>    # клонировать репозиторий
cd <имя_проекта>               # перейти в папку проекта

python3 -m venv venv           # создать виртуальное окружение
source venv/bin/activate       # активировать окружение

pip install -r requirements.txt  # установить зависимости

cp .env.example .env           # скопировать настройки окружения (если есть .env.example)
#отредактировать .env и добавить свои ключи / настройки


python manage.py migrate       # применить миграции
python manage.py createsuperuser  # создать суперпользователя (опционально)

python manage.py runserver     # запустить сервер разработки (http://127.0.0.1:8000/admin)

и в файле main нажать плей)
готово, бот запущен

#опционально
python manage.py test          # запустить тесты
