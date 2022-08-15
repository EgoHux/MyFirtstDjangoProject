from django.urls import path
import adminapp.views as adminapp


app_name = "adminapp"

urlpatterns = [

    path('users/', adminapp.View_Users.as_view(), name='view_users'),
    path('users/<int:page>', adminapp.View_Users.as_view(), name='view_users'),
    path("create_user/", adminapp.Create_User.as_view(), name='create_user'),
    path('update_user/<int:pk>', adminapp.Update_User.as_view(), name='update_user'),
    path('delete_user/<int:pk>', adminapp.delete_user, name='delete_user'),


    path('category/', adminapp.View_Category.as_view(), name='view_category'),
    path("create_category/", adminapp.Create_Category.as_view(), name='create_category'),
    path('update_category/<int:pk>', adminapp.Update_Category.as_view(), name='update_category'),
    path('delete_category/<int:pk>', adminapp.delete_category, name='delete_category'),


    path('<int:pk>/products/', adminapp.view_products, name='view_products'),
    path("create_product/", adminapp.create_product, name='create_product'),
    path('update_product/<int:pk>', adminapp.update_product, name='update_product'),
    path('delete_product/<int:pk>', adminapp.delete_product, name='delete_product'),
]