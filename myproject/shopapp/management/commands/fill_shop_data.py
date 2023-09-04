from typing import Any, Optional
from django.core.management.base import BaseCommand
from shopapp.models import Client, Product, Order
from django.conf import settings
import random

class Command(BaseCommand):
    help = "Generate fake data for shopapp"
    
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Data count')
        
    def handle(self, *args, **kwargs):
        if not settings.DEBUG:
            self.stderr.write('Use in DEBUG mode only')
            return
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(
                name=f'Client{i}',
                email=f'mail{i}@mail.ru')
            client.save()
            product = Product(
                name=f'Product{i}', 
                desc=f'Product description {i}',
                price = round(random.uniform(1, 10000.99), 2),
                count = random.randint(1, 100))
            product.save()
            order = Order(
                client = Client.objects.filter(pk=random.randint(1, count)).first()
                
            )
            order.save
            