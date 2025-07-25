from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Удаляет все данные и добавляет тестовые категории и продукты'

    def handle(self, *args, **options):
        self.stdout.write('Удаляем все продукты и категории...')
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write('Создаем категории...')
        electronics = Category.objects.create(
            name="Электроника",
            description="Современные электронные устройства и гаджеты — смартфоны, ноутбуки, аудиотехника и аксессуары."
        )
        clothing = Category.objects.create(
            name="Одежда и обувь",
            description="Модная одежда, обувь и аксессуары для мужчин, женщин и детей на любой сезон."
        )
        home_garden = Category.objects.create(
            name="Дом и сад",
            description="Товары для дома и дачи — мебель, инструменты, украшения и садовая техника."
        )
        books = Category.objects.create(
            name="Книги и канцелярия",
            description="Книги различных жанров, учебная и офисная канцелярия."
        )
        beauty_health = Category.objects.create(
            name="Красота и здоровье",
            description="Косметика, средства ухода и товары для здоровья и фитнеса."
        )
        children_goods = Category.objects.create(
            name="Детские товары",
            description="Игрушки, одежда и товары для новорождённых и детей разных возрастов."
        )

        self.stdout.write('Создаем продукты...')

        Product.objects.create(
            name="Смартфон X100",
            description="Современный смартфон с большим экраном, 128 ГБ памяти и мощной камерой.",
            category=electronics,
            price=29999,
        )
        Product.objects.create(
            name="Куртка зимняя мужская",
            description="Теплая и комфортная зимняя куртка, размер M-XL, цвет черный.",
            category=clothing,
            price=7999,
        )
        Product.objects.create(
            name="Стул деревянный Classic",
            description="Удобный деревянный стул из натурального массива дуба для дома и офиса.",
            category=home_garden,
            price=3500,
        )
        Product.objects.create(
            name="Роман 'Война и мир'",
            description="Классический роман Льва Толстого, издание в мягкой обложке.",
            category=books,
            price=450,
        )
        Product.objects.create(
            name="Увлажняющий крем для лица",
            description="Легкий увлажняющий крем с алоэ вера для всех типов кожи.",
            category=beauty_health,
            price=1200,
        )
        Product.objects.create(
            name="Набор мягких игрушек",
            description="Мягкие и безопасные игрушки для малышей от 0 до 3 лет.",
            category=children_goods,
            price=2500,
        )

        self.stdout.write(self.style.SUCCESS('Данные успешно обновлены.'))
