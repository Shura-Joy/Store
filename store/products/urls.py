from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("", views.products, name="index"),
    path("products/basket/add/<int:product_id>/",
         views.basket_add, name="basket_add"),
    path("products/basket/remove/<int:basket_id>/",
         views.basket_remove, name="basket_remove"),
]
