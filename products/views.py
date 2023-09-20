from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()    # This will return all the products from the database

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)    # This will return the product with the id that matches the product_id passed in the url

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)