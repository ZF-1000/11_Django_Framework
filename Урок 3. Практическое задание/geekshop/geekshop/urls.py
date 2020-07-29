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
from django.urls import path, include        # Метод с помощью которого определяются урлы

import mainapp.views as mainapp
# from mainapp import views - второй вариант

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),    # Админка
    # path - задает сопоставление определенного маршрута с функцией обработки.
    # Функция path() располагается в пакете django.urls и принимает два параметра: запрошенный адрес URL
    # и функция, которая обрабатывает запрос по этому адресу (вьюшка, которая будет отвечать за отображение).
    # Дополнительно через третий параметр можно указать имя маршрута
    # path('относительный адрес на который будет переходить пользователь')
    # path('') - так обозначается корневая страничка сайта
    # / - корневая папка проекта. Абсолютный адрес от корня проекта
    path('', mainapp.main, name='main'),                    # корневой url
    path('contacts/', mainapp.contacts, name='contacts'),

    # path('products/', mainapp.products, name='products'),
    # path('products/all/', mainapp.products, name='products_all'),
    # path('products/home/', mainapp.products, name='products_home'),
    # path('products/office/', mainapp.products, name='products_office'),
    # path('products/modern/', mainapp.products, name='products_modern'),
    # path('products/classic/', mainapp.products, name='products_classic'),
    path('products/', include('mainapp.urls')),

    path('products/product-11/', mainapp.products, name='product-11'),
    path('products/product-21/', mainapp.products, name='product-21'),
    path('products/product-31/', mainapp.products, name='product-31'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
