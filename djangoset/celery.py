# import os
# from celery import Celery
#
#
# # Установка переменной окружения, чтобы Celery знал, где находится файл настроек Django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoset.settings')
#
# # Создание экземпляра Celery
# app = Celery('djangoset')
#
# # Загрузка настроек Celery из файла settings.py
# app.config_from_object('django.conf:settings', namespace='CELERY')
#
# # Автоматическое обнаружение и регистрация задач из приложений Django
# app.autodiscover_tasks()
#
# # Для отладки (чтобы видеть, когда задачи запускаются)
# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
