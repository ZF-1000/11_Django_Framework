import json
import os
import random

from django.shortcuts import render, get_object_or_404
# Create your views here.
# request - это параметр в котором хранится вся информация о запросе, который отправил пользователь
# (сессии, форма на заполнение, адрес по которому переходили, вся мета информация о запросе)
# вьюшка - по сути это метод (функция)
import datetime

from geekshop.settings import BASE_DIR
from .models import ProductCategory, Product
from basketapp.models import Basket


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    '''Получение горячего предложения'''
    products_list = Product.objects.all()
    return random.sample(list(products_list), 1)[0]


def get_same_products (hot_product):
    '''Получение похожих товаров на основе полученного горячего предложения'''
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[: 3]
    return same_products


def main(request):
    title = 'главная'
    products = Product.objects.all()[:3]
    context = {'title': title, 'products': products, 'basket': get_basket(request.user)}
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()  # все категории, которые были заполнены

    basket = get_basket(request.user)

    context = {
        'title': title,
        'links_menu': links_menu,
        'basket': basket
    }

    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all()
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category_id=pk)

        context['category'] = category
        context['products'] = products_list
        return render(request, 'mainapp/products_list.html', context)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    context['same_products'] = same_products
    context['hot_product'] = hot_product

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
        'locations': locations,
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/contact.html', context)


def product(request, pk):
    title = 'продукты'
    context = {
        'title': 'Продукт',
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/product.html', context)
