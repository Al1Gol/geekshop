from django.db import migrations


def forwards_func(apps, schema_editor):
    pro_cat_model = apps.get_model("mainapp", "ProductCategory")  # Load model for make changes
    pro_model = apps.get_model("mainapp", "Products")  # Load model for make changes
    con_model = apps.get_model("mainapp", "Contact")  # Load model for make changes

    # Create new category
    pro_cat_obj = pro_cat_model.objects.create(pk=1, name="дом", description="отличная мебель для домашнего интерьера.")
    # Create new products in this category
    pro_model.objects.create(
        pk=1,
        category=pro_cat_obj,  # Foreign key
        name="комфорт 1",
        image="products_images/product-1.jpg",
        short_desc="комфортный стул",
        description="подойдет для просмотра фильмов",
        price="2989.50",
        quanity=17,
    )
    pro_model.objects.create(
        pk=2,
        category=pro_cat_obj,  # Foreign key
        name="комфорт 2",
        image="products_images/product-2.jpg",
        short_desc="очень комфортный стул",
        description="подойдет для общения с друзьями",
        price="3687.2",
        quanity=21,
    )
    pro_model.objects.create(
        pk=3,
        category=pro_cat_obj,  # Foreign key
        name="люкс",
        image="products_images/product-3.jpg",
        short_desc="использованы премиальные материалы",
        description="для тех, кто стремится к лучшему",
        price="8157.99",
        quanity=7,
    )
    del pro_cat_obj  # Delete link for category

    # Create new category
    pro_cat_obj = pro_cat_model.objects.create(
        pk=2, name="офис", description="стильная и надежная офисная мебель нового поколения."
    )
    # Create new products in this category
    pro_model.objects.create(
        pk=4,
        category=pro_cat_obj,  # Foreign key
        name="стандарт",
        image="products_images/product-4.jpg",
        short_desc="универсальное решение",
        description="подойдет для любого офиса",
        price="1895.25",
        quanity=27,
    )
    pro_model.objects.create(
        pk=5,
        category=pro_cat_obj,  # Foreign key
        name="премиум",
        image="products_images/product-5.jpg",
        short_desc="улучшенный дизайн",
        description="идеально впишется в строгий интерьер офиса",
        price="3587.41",
        quanity=9,
    )
    del pro_cat_obj  # Delete link for category

    # Create new category
    pro_cat_obj = pro_cat_model.objects.create(
        pk=3, name="модерн", description="мебель в стиле МОДЕРН подойдет для любого интерьера."
    )
    # Create new products in this category
    pro_model.objects.create(
        pk=6,
        category=pro_cat_obj,  # Foreign key
        name="новинка",
        image="products_images/product-6.jpg",
        short_desc="инновационный дизайн",
        description="нестандартное решение для современного интерьера",
        price="5361.47",
        quanity=18,
    )
    pro_model.objects.create(
        pk=7,
        category=pro_cat_obj,  # Foreign key
        name="прогресс",
        image="products_images/product-7.jpg",
        short_desc="прогрессивный дизайн",
        description="функциональное и комфортное решение",
        price="6789.33",
        quanity=12,
    )
    del pro_cat_obj  # Delete link for category

    # Create new category
    pro_cat_obj = pro_cat_model.objects.create(
        pk=4, name="классика", description="классический стиль актуален в любые времена."
    )
    # Create new products in this category
    pro_model.objects.create(
        pk=8,
        category=pro_cat_obj,  # Foreign key
        name="венеция",
        image="products_images/product-8.jpg",
        short_desc="классические формы",
        description="окунитесь в европейский комфорт",
        price="4147.51",
        quanity=25,
    )
    pro_model.objects.create(
        pk=9,
        category=pro_cat_obj,  # Foreign key
        name="тоскана",
        image="products_images/product-9.jpg",
        short_desc="эргономичная спинка",
        description="почувствуйте комфорт и насладитесь цветовой гаммой",
        price="7147.35",
        quanity=18,
    )
    pro_model.objects.create(
        pk=10,
        category=pro_cat_obj,  # Foreign key
        name="рим",
        image="products_images/product-10.jpg",
        short_desc="удачные пропорции",
        description="компактность и функциональность",
        price="8357.77",
        quanity=8,
    )

    # Create contacts
    con_model.objects.create(
        pk=1, phone="+7-888-888-8888", email="info@geekshop.ru", city="Москва", address="В пределах МКАД"
    )
    con_model.objects.create(
        pk=2,
        phone="+7-777-777-7777",
        email="info_yekaterinburg@geekshop.ru",
        city="Екатеринбург",
        address="Близко к центру",
    )
    con_model.objects.create(
        pk=3,
        phone="+7-999-999-9999",
        email="info_vladivostok@geekshop.ru",
        city="Владивосток",
        address="Близко к океану",
    )


def reverse_func(apps, schema_editor):
    pro_cat_model = apps.get_model("mainapp", "ProductCategory")  # Load model for make changes
    con_model = apps.get_model("mainapp", "Contact")  # Load model for make changes

    # Delete all objects
    pro_cat_model.objects.all().delete()
    con_model.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [("mainapp", "0003_contact")]

    operations = [migrations.RunPython(forwards_func, reverse_func)]