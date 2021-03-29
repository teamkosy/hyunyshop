from django.shortcuts import render, get_object_or_404
from .models import *


def product_in_category(request, category, slug=None):
    current_category = None
    categories = Category.object.all()
    products = Product.object.filter(available_display=True)
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(request, 'shop/list.html', {'current_category':current_category,'categories':categories,'products':products})


def product_detail(request, id, product slug=None):
    product = get_object_or_404(Product, id=id, slug=prouct_slug)

    return render(request, 'shop/detail.html', {'product':product})

