from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()    # This will return all the products from the database
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')    # This will split the category string into a list of individual categories
            products = products.filter(category__name__in=categories)    # This will filter the products by the categories that are in the categories list
            categories = Category.objects.filter(name__in=categories)    # This will return the categories that are in the categories list
        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,    # This will be used to display the search term in the search box after the search has been performed
        'current_categories': categories,    # This will be used to display the categories that are currently being filtered by in the category filter menu
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)    # This will return the product with the id that matches the product_id passed in the url

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)