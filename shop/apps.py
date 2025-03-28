# shop/apps.py
from django.apps import AppConfig
import importlib


class ShopConfig(AppConfig):
    name = 'shop'

    def ready(self):
        importlib.import_module('shop.signals')
