from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'


urlpatterns = [
    path('', mainapp.products, name='index'),
    path('<int:pk>/', mainapp.products, name='category'),

    path('products/product-11/', mainapp.products, name='product-11'),
    path('products/product-21/', mainapp.products, name='product-21'),
    path('products/product-31/', mainapp.products, name='product-31'),
]

