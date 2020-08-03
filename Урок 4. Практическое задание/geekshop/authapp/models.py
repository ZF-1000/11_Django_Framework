from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)   # аватарка
    age = models.PositiveIntegerField(verbose_name='возраст')           # возраст
