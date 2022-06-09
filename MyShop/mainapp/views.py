from django.shortcuts import render
from .models import Product, Category

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', context={
        'title': "Главная"
    })

def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'mainapp/products.html', context={
        'title': "Продукты",
        'products': products,
        'categories': categories
    })

def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': "Контакты"
    })
