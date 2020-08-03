"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# из модуля django.contrib импортируется класс AdminSite, который предоставляет возможности работы
# с интерфейсом администратора
from django.contrib import admin    # Стандартная админка django (способна администрировать сайт)
# из модуля django.urls импортируется функция path. Эта функция задает сопоставление определенного
# маршрута с функцией обработки
from django.urls import path        # Метод с помощью которого определяются урлы

import mainapp.views as mainapp
# from mainapp import views - второй вариант

urlpatterns = [
    path('admin/', admin.site.urls),    # Админка

# Функция path() располагается в пакете django.urls и принимает два параметра: запрошенный адрес URL и функция,
# которая обрабатывает запрос по этому адресу. Дополнительно через третий параметр можно указать имя маршрута
    # path('относительный адрес на который будет переходить пользователь')
    # path('') - так обозначается корневая страничка сайта
    # / - корневая папка проекта
    path('', mainapp.main),
    path('products/', mainapp.products),
    path('contact/', mainapp.contacts),
]
