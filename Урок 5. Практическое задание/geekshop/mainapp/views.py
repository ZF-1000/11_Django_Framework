import json
import os

from django.shortcuts import render, get_object_or_404
# Create your views here.
# request - это параметр в котором хранится вся информация о запросе, который отправил пользователь
# (сессии, форма на заполнение, адрес по которому переходили, вся мета информация о запросе)
# вьюшка - по сути это метод (функция)
import datetime

from geekshop.settings import BASE_DIR
from .models import ProductCategory, Product
from basketapp.models import Basket


def main(request):
    title = 'главная'
    products = Product.objects.all()[:3]
    context = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    title = 'продукты'
    links_menu = ProductCategory.objects.all()  # все категории, которые были заполнены

    context = {
        'title': title,
        'links_menu': links_menu,
        'basket': basket
    }

    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all()
            category = {
                'name': 'все'
            }
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category_id=pk)
        context['category'] = category
        context['products'] = products_list
        return render(request, 'mainapp/products_list.html', context)

    same_products = Product.objects.all()[3:6]

    context['same_products'] = same_products

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
