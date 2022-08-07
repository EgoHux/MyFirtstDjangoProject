from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from django.contrib.auth.decorators import login_required



# Create your views here.

def login(request):
    form = ShopUserLoginForm()
    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                auth.login(request, user=user)
                reverse_url = request.GET.get('next', reverse('main'))
                return HttpResponseRedirect(reverse_url)

    return render(request, 'authapp/login.html', context={
            'title': "Вход в систему",
            'form': ShopUserLoginForm()
    })
    # content = {'title': title, 'login_form': login_form, 'form': ShopUserLoginForm}


def register(request):
    form = ShopUserRegisterForm()
    if request.method == 'POST':
        form = ShopUserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:login'))

    return render(request, 'authapp/register.html', context={
            'title': "Регистрация",
            'form': form
    })

@login_required
def edit(request):
    form = ShopUserEditForm(instance=request.user)
    if request.method == 'POST':
        form = ShopUserEditForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main'))

    return render(request, 'authapp/edit.html', context={
            'title': "Редактирование пользователя",
            'form': form
    })

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))

