from catalog.models import Product
from config.settings import CACHE_ENABLED
from django.core.cache import cache


def get_products_by_category(category_name):
    """Возвращает список продуктов заданной категории"""
    return Product.objects.filter(category__name__iexact=category_name)


def get_products_from_cache():
    """Получает данные из кэша, если данные в кэше отсутствуют, получает их из БД"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products



