from django.shortcuts import render, HttpResponseRedirect

from .models import Product, ProductCategory, Basket

from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    context = {'title': 'Store'}
    return render(request, "products/index.html", context)


def products(request):
    context = {'title': 'Store - Каталог', 'products': Product.objects.all,
               'categories': ProductCategory.objects.order_by('name')}
    return render(request, "products/products.html", context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(pk=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product).first()
    if baskets:
        baskets.quantity += 1
        baskets.save()
    else:
        Basket.objects.create(user=request.user, product=product, quantity=1)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    Basket.objects.get(user=request.user, pk=basket_id).delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
