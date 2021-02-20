from django.contrib import admin

from .models import Contact, ProductCategory, Products

# Registefrom django.contrib import admin

admin.site.register(ProductCategory)
admin.site.register(Products)
admin.site.register(Contact)
