from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', context={
        'title': "Главная"
    })

def products(request):
    return render(request, 'mainapp/products.html', context={
        'title': "Продукты",
        'products': [
            {'name': "Стул повышенного качества", 'description': "Не оторваться.", 'image': 'img/product-11.jpg'},
            {'name': "Стул повышенного качества 2 ", 'description': "Не оторваться. 2", 'image': 'img/product-21.jpg'},
            {'name': "Стул повышенного качества 3 ", 'description': "Не оторваться. 3", 'image': 'img/product-31.jpg'}
        ]
    })

def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': "Контакты"
    })
