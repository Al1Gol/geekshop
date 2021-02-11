from django.contrib import admin
from .models import Contact, Products, ProductCategory
from .models import Products, ProductCategory

# Registefrom django.contrib import admin

admin.site.register(ProductCategory)
admin.site.register(Products)
admin.site.register(Contact)