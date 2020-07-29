from django.shortcuts import render

# Create your views here.
# request - это параметр в котором хранится вся информация о запросе, который отправил пользователь
# (сессии, форма на заполнение, адрес по которому переходили, вся мета информация о запросе)
# вьюшка - по сути это метод (функция)


def main(request):
    context = {
        'title': 'главная'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    same_products = [
        {'href': 'product-11', 'name': 'продукт-11'},
        {'href': 'product-21', 'name': 'продукт-21'},
        {'href': 'product-31', 'name': 'продукт-31'},
    ]
    submenu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    context = {
        'title': 'продукты',
        'same_products': same_products,
        'submenu': submenu
    }
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    context = {
        'title': 'контакты'
    }
    return render(request, 'mainapp/contact.html', context)
