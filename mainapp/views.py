import random

from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Contact, ProductCategory, Products


def main(request):
    title = "главная"
    products = Products.objects.filter(is_active=True, category__is_active=True)[:3]
    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL}
    return render(request, "mainapp/index.html", content)


# def get_hot_product():
#     products = Product.objects.filter(is_active=True, category__is_active=True)
#     return random.sample(list(products), 1)[0]


# def get_same_products(hot_product):
#     same_products = Product.objects.filter(category=hot_product.category, is_active=True).exclude(pk=hot_product.pk)[:3]
#     return same_products


def get_hot_product_list():
    products = Products.objects.filter(is_active=True, category__is_active=True).select_related("category")
    hot_product = random.sample(list(products), 1)[0]
    hot_list = products.exclude(pk=hot_product.pk)[:3]
    return (hot_product, hot_list)


def products(request, pk=None, page=1):
    title = "продукты"
    links_menu = ProductCategory.objects.filter(is_active=True)

    if pk is not None:
        if str(pk) == str(0):
            category = {"pk": 0, "name": "все"}
            products = Products.objects.filter(is_active=True, category__is_active=True).order_by("price")
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Products.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by(
                "price"
            )

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            "title": title,
            "links_menu": links_menu,
            "category": category,
            "products": products_paginator,
            "media_url": settings.MEDIA_URL,
        }
        return render(request, "mainapp/products_list.html", content)
    # hot_product = get_hot_product()
    # same_products = get_same_products(hot_product)
    hot_product, same_products = get_hot_product_list()
    content = {
        "title": title,
        "links_menu": links_menu,
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,
        "hot_product": hot_product,
    }
    return render(request, "mainapp/products.html", content)


def product(request, pk):
    title = "продукты"
    content = {
        "title": title,
        "links_menu": ProductCategory.objects.filter(is_active=True),
        "product": get_object_or_404(Products, pk=pk),
        "media_url": settings.MEDIA_URL,
    }
    return render(request, "mainapp/product.html", content)


from django.views.decorators.cache import cache_page


@cache_page(600)
def contact(request):
    title = "о нас"
    visit_date = timezone.now()
    locations = Contact.objects.all()
    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contact.html", content)
