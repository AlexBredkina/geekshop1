from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title': 'Главная страница',
    }

    return render(request, 'mainapp/index.html', context)


def products(request):
    content = {
        'title': 'Товары',
        'products': [{'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00 руб.', 'card': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.', 'image':'/static/vendor/img/products/Adidas-hoodie.png'},
                     {'name': 'Синяя куртка The North Face', 'price': '23 725,00 руб.', 'card': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.', 'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png'},
                     {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00 руб.','card': 'Материал с плюшевой текстурой. Удобный и мягкий.', 'image' : '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
                     {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00 руб.', 'card': 'Плотная ткань. Легкий материал.', 'image': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png'},
                     {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00 руб.', 'card': 'Гладкий кожаный верх. Натуральный материал.', 'image': '/static/vendor/img/products/Black-Dr-Martens-shoes.png'},
                     {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890,00', 'card': 'Легкая эластичная ткань сирсакер Фактурная ткань.', 'image': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'},
                     ],
    }
    products = content['products']
    return render(request, 'mainapp/products.html', content)


def test_context(request):
    context = {
        'title': 'добро пожаловать!',
        'username': 'Valeriy Pavlikov',
        'products': [{'name': 'Черное худи', 'price': '2 9990 руб.'},
                     {'name': 'Джинсы', 'price': '5 800 руб.'},

                     ],
        'promotion': True,
        'promotion_products': [
            {'name': 'Туфли Dr Martnes', 'price': '10 000 руб.'},
        ],

    }
    products = context['products']
    return render(request, 'mainapp/context.html', context)
