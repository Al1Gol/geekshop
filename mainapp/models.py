from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.
class ProductCategory(models.Model):
    name = CharField(verbose_name='имя', max_length=64, unique=True)
    description = TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="название продукта", max_length=128)
    image = models.ImageField(verbose_name="изображение", upload_to = "products_images", blank=True)
    short_desc = models.CharField(verbose_name="краткое описание", max_length=128, blank=True)
    description = models.TextField(verbose_name="описание продукта", blank=True)
    price = models.DecimalField(verbose_name="цена продукта", max_digits=8, decimal_places=2, default=0)
    quanity = models.PositiveIntegerField(verbose_name="количество на складе", default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"