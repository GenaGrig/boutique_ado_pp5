from django.shortcuts import render
from .models import Product


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()    # This will return all the products from the database

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)