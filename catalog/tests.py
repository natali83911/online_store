from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Category, Product

User = get_user_model()


class ProductModelTests(TestCase):
    def setUp(self):
        # Создаём пользователя напрямую
        self.user = User(
            email="testuser@example.com",
            is_active=True,
        )
        self.user.set_password("pass")
        self.user.save()

        # Создаём категорию
        self.category = Category.objects.create(
            name="Категория 1", description="Описание"
        )

        # Создаём продукт
        self.product = Product.objects.create(
            name="Продукт 1",
            description="Описание продукта",
            category=self.category,
            price=100,
            status="draft",
            owner=self.user,
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Продукт 1")
        self.assertEqual(self.product.category.name, "Категория 1")
        self.assertEqual(self.product.owner.email, "testuser@example.com")

    def test_product_str(self):
        self.assertEqual(str(self.product), "Продукт 1 Категория 1")

    def test_product_ordering(self):
        products = Product.objects.all()
        self.assertIn(self.product, products)
