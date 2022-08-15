
from django.http.response    import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from mainapp.models import Category, Product
from authapp.models import ShopUser
from authapp.forms import ShopUserEditForm, ShopUserRegisterForm
from mainapp.forms import ProductForm
from .utils import check_superuser
from django.utils.decorators import method_decorator 


# Create your views here.


class SuperUserRequiredMixin:
    @method_decorator(check_superuser)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class TitleMixin:
    title = None
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context
    
    
class View_Users(SuperUserRequiredMixin, TitleMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/view_users.html'
    title = 'Пользователи'
    paginate_by = 2




class Create_User(SuperUserRequiredMixin, TitleMixin, CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'adminapp/create_user.html'
    success_url = reverse_lazy('adminka:view_users')
    title = "Создать пользователя"
    

class Update_User(SuperUserRequiredMixin, TitleMixin, UpdateView):
    model = ShopUser
    template_name = 'adminapp/update_user.html'
    success_url = reverse_lazy('adminka:view_users')
    title = 'Обновить пользователя'
    form_class = ShopUserEditForm


@check_superuser
def delete_user(request, pk):
    user = get_object_or_404(ShopUser,pk=pk)
    user.is_active = False    
    user.save()
    return HttpResponseRedirect(reverse('adminka:view_users'))


class View_Category(SuperUserRequiredMixin, TitleMixin, ListView):
    model = Category
    template_name = 'adminapp/view_category.html'
    title = "Категории"

    
class Create_Category(SuperUserRequiredMixin, TitleMixin, CreateView):
    model = Category
    fields = "__all__"
    template_name = 'adminapp/create_category.html'
    success_url = reverse_lazy('adminka:view_category')
    title = 'Создать категорию'


class Update_Category(SuperUserRequiredMixin, TitleMixin, UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'adminapp/update_category.html'
    success_url = reverse_lazy('adminka:view_category')
    title = 'Обновить категорию'



@check_superuser
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.is_active = False
    category.save()

    return HttpResponseRedirect(reverse("adminka:view_category")) 

@check_superuser
def view_products(request, pk):
    category = Category.objects.get(pk=pk)
    product = Product.objects.filter(category=category)

    return render(request, 'adminapp/view_products.html', context={
        'title':f"Продукты категории {category.name}",
        'products':product,
        'category':category
    })

@check_superuser
def create_product(request):
    form = ProductForm()
    # category = get_object_or_404(Category, pk=category_id)
    if request.method == "POST":
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("adminka:view_category"))

    return render(request, 'adminapp/create_product.html', context={
        'title':"Cоздания продукта",
        'form':form,
        
    })

@check_superuser
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form=ProductForm(instance=product)
    if request.method =="POST":
        form = ProductForm(data=request.POST, files=request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminka:view_products', args=[product.category.pk]))

    return render(request, 'adminapp/update_product.html', context={
        'title': "Редактирование продукта",
        'form':form,
        'product':product
        
    })

@check_superuser
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return HttpResponseRedirect(reverse('adminka:view_products', args=[product.category.pk]))