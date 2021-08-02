from django.shortcuts import render, get_list_or_404
from .models import Product


def all_products(request):
    """ Returns a view with information about a individual product """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_info(request, product_id):
    """ Returns a view of all products """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)