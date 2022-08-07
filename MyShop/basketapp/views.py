from django.shortcuts import render, get_object_or_404
from .models import Basket
from mainapp.models import Product
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def view(request):
    return render(request, "basketapp/basket.html", context={
        'basket': Basket.objects.filter(user = request.user)
    })

@login_required
def add(request, product_id):
    product = get_object_or_404(Product, pk = product_id)
    basket = Basket.objects.filter(user=request.user, product=product)
    if basket:
        basket_item = basket[0]
        basket_item.quantity +=1
        basket_item.save()
    else:
        basket_item = Basket(user=request.user, product=product)
        basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('main')))

@login_required
def delete(request, basket_id):
    basket = get_object_or_404(Basket, pk = basket_id)
    basket.quantity -= 1
    if not basket.quantity:
        basket.delete()
    else:
        basket.save()
    return HttpResponseRedirect(reverse("basket:view"))

@login_required
def edit(request, basket_id, quantity):
    if request.is_ajax():
        basket = get_object_or_404(Basket, pk = basket_id)
        basket.quantity = quantity
        if not basket.quantity:
            basket.delete()
        else:
            basket.save()
        return render(request, 'mainapp/includes/basket_inc.html')