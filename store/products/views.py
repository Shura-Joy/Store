from django.shortcuts import render

from . import models

# Create your views here.


def index(request):
    return render(request, "products/index.html")


def products(request):
    context = {'products': models.Product.objects.all,
               'categories': models.ProductCategory.objects.order_by('name')}
    return render(request, "products/products.html", context)
