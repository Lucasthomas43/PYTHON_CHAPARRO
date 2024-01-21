from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products/", views.product_list, name="products_list"),
    path("products/create", views.product_create, name="product_create"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register")
   
]
