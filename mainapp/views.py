from django.shortcuts import render
from mainapp.models import ProductCategory, Product


# Create your views here.
def index(request):
    context = {
        'title': 'Главная страница',
    }

    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    context = {
        'title': 'Товары',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context=context)


# def test_context(request):
#     context = {
#         'title': 'добро пожаловать!',
#         'username': 'Valeriy Pavlikov',
#         'products': [{'name': 'Черное худи', 'price': '2 9990 руб.'},
#                      {'name': 'Джинсы', 'price': '5 800 руб.'},
#
#                      ],
#         'promotion': True,
#         'promotion_products': [
#             {'name': 'Туфли Dr Martnes', 'price': '10 000 руб.'},
#         ],
#
#     }
#     products = context['products']
#     return render(request, 'mainapp/context.html', context)
