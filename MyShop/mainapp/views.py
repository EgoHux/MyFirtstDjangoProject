import random

from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', context={
        'title': "Главная"
    })

def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    hot_product = random.choice(products)
    products = products.exclude(pk=hot_product.pk)
    return render(request, 'mainapp/products.html', context={
        'title': "Продукты",
        'products': products,
        "hot_product":hot_product,
        'categories': categories
    })

def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = Category.objects.all()
    return render(request, 'mainapp/product.html', context={
        'title': product.name,
        'links_menu': Category.objects.all(),
        'product': product,
        'categories': categories

    })

def category(request, pk):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=pk)
    products = Product.objects.filter(category=category)
    return render(request, 'mainapp/category.html', context={
        'title': "Продукты",
        'products': products,
        'categories': categories,
        "category": category
    })

def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': "Контакты"
    })
