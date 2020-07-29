import json
import os

from django.shortcuts import render
# Create your views here.
# request - это параметр в котором хранится вся информация о запросе, который отправил пользователь
# (сессии, форма на заполнение, адрес по которому переходили, вся мета информация о запросе)
# вьюшка - по сути это метод (функция)
import datetime

from geekshop.settings import BASE_DIR
from .models import ProductCategory, Product


def main(request):
    title = 'главная'
    products = Product.objects.all()[: 4 ]
    context = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', context)


def products(request):
    title = 'продукты'
    submenu = [
        {'href': 'mainapp:products_all', 'name': 'все'},
        {'href': 'mainapp:products_home', 'name': 'дом'},
        {'href': 'mainapp:products_office', 'name': 'офис'},
        {'href': 'mainapp:products_modern', 'name': 'модерн'},
        {'href': 'mainapp:products_classic', 'name': 'классика'},
    ]
    same_products = []
    products_file_path = os.path.join(BASE_DIR, 'products.json')
    if os.path.exists(products_file_path):
        with open(products_file_path, encoding="utf-8") as products_file:
            same_products = json.loads(products_file.read())

    context = {
        'title': title,
        'submenu': submenu,
        'same_products': same_products
    }
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    title = 'о нас'
    visit_date = datetime.datetime.now()
    locations = []
    contacts_file_path = os.path.join(BASE_DIR, 'contacts.json')
    if os.path.exists(contacts_file_path):                  # проверка существования файла
        with open(contacts_file_path, encoding="utf-8") as contacts_file:     # открыл файл
            locations = json.loads(contacts_file.read())    # распарсил как json
    context = {
        'title': title,
        'visit_date': visit_date,
        'locations': locations
    }
    return render(request, 'mainapp/contact.html', context)
