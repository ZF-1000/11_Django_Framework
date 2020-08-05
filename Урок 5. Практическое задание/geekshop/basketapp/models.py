from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket', verbose_name='Пользователь',)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт',)
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество',)
    add_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
