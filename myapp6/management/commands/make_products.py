from random import choice, randint, uniform

from django.core.management.base import BaseCommand
from myapp5.models import Category, Product

class Command(BaseCommand):
    help = 'Generate fake products'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Количество товаров для генерации')

    def handle(self, *args, **kwargs):
        categories = Category.objects.all()
        products = []
        count = kwargs.get('count')
        for i in range(1, count + 1):
            products.append(Product(
                name=f'Продукт номер {i}',
                category=choice(categories),
                description=f'длинное описание продукта номер {i} которое никто не читает',
                price=uniform(0.01, 99.9),
                quantity=randint(1, 99),
                rating=uniform(0.01, 9.99),
            ))
        Product.objects.bulk_create(products)

