from django.urls import path
import basketapp.views as basketapp


app_name = "basketapp"

urlpatterns = [
    path('', basketapp.view, name = 'view'),
    path('add/<int:product_id>/', basketapp.add, name = 'add'),
    path('delete/<int:basket_id>/', basketapp.delete, name = 'delete'),
    path('edit/<int:basket_id>/<int:quantity>/', basketapp.edit, name='edit')

]