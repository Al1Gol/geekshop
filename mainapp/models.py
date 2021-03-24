from django.db import models
from django.db.models.fields import CharField, TextField


# Create your models here.
class ProductCategory(models.Model):
    name = CharField(verbose_name="имя", max_length=64, unique=True)
    description = TextField(verbose_name="описание", blank=True)
    is_active = models.BooleanField(verbose_name="категория активна", default=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="название продукта", max_length=128)
    image = models.ImageField(verbose_name="изображение", upload_to="products_images", blank=True)
    short_desc = models.CharField(verbose_name="краткое описание", max_length=128, blank=True)
    description = models.TextField(verbose_name="описание продукта", blank=True)
    price = models.DecimalField(verbose_name="цена продукта", max_digits=8, decimal_places=2, default=0)
    quanity = models.PositiveIntegerField(verbose_name="количество на складе", default=0)
    is_active = models.BooleanField(verbose_name="продукт активен", default=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"
    
    @staticmethod
    def get_items():
        return Products.objects.filter(is_active=True).order_by("category", "name")


class Contact(models.Model):
    phone = models.CharField(max_length=50, verbose_name="номер телефона")
    email = models.EmailField(max_length=254, verbose_name="электронная почта")
    city = models.CharField(max_length=128, default="Москва", verbose_name="город")
    address = models.CharField(max_length=254, verbose_name="адресс")

    def __str__(self):
        return f"{self.pk} {self.email}"
        return f"{self.name} ({self.category.name})"
