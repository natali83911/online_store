from django.db import models
from django.conf import settings


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="product/image",
        null=True,
        blank=True,
        verbose_name="Фото продукта",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        verbose_name="Наименование категории продукта",
        help_text="Введите категорию продукта",
        related_name="products",
    )
    price = models.IntegerField(
        verbose_name="Стоимость продукта", help_text="Введите стоимость продукта"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания продукта"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения продукта"
    )
    STATUS_CHOICES = [
        ("draft", "Черновик"),
        ("published", "Опубликован"),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="draft",
        verbose_name="Статус публикации",
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Владелец продукта",
    )

    def __str__(self):
        return f"{self.name} {self.category}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "name",
            "category",
            "price",
        ]
        permissions = [
            ("can_unpublish_product", "Может отменять публикацию продукта"),
        ]


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории", help_text="Введите описание"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = [
            "name",
        ]
