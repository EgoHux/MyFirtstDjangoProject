from django.core.management.base import BaseCommand
from django.conf import settings
from mainapp.models import Category, Product
import json
from django.contrib.auth import get_user_model
from authapp.models import ShopUser


class Command(BaseCommand):
    def handle(self, *args, **options):

        #Загрузка категорий из json файла
        with open(settings.DATA_ROOT / 'categories.json', 'r', encoding='utf-8') as file:
            categories = json.load(file)
            for category in categories:
                if not Category.objects.filter(name = category["name"]):
                    Category(name = category["name"], description = category['description']).save()

        #Загрузка продуктов из json файла

        with open(settings.DATA_ROOT / "products.json", 'r', encoding="utf-8") as file:
            products = json.load(file)
            for product in products:
                product["category"] = Category.objects.get(name = product["category"])
                Product(**product).save()


        #Создание суперпользователя
        if not get_user_model().objects.filter(username = 'admin'):
            get_user_model().objects.create_superuser(username='admin', password='admin')
