from django.shortcuts import render

from . import models

# Create your views here.


def index(request):
    context = {'title': 'Store'}
    return render(request, "products/index.html", context)


def products(request):
    context = {'title': 'Store - Каталог', 'products': models.Product.objects.all,
               'categories': models.ProductCategory.objects.order_by('name')}
    return render(request, "products/products.html", context)
