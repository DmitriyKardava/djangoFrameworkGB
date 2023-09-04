from django.core.management.base import BaseCommand
from shopapp.models import Order, OrderItems


class Command(BaseCommand):
    help = "Get order by id."
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')
        
    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        order = Order.objects.filter(pk=pk).first()
        self.stdout.write(f'{order}')
        if order is not None:
            items = OrderItems.objects.filter(order=order)
            self.stdout.write(f'{items}')
