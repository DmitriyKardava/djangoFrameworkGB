from django.core.management.base import BaseCommand
from shopapp.models import Client

class Command(BaseCommand):
    help = "Create client."
    
    def handle(self, *args, **kwargs):
        client = Client(name='John', email='john@example.com', password='secret', age=25)
        client.save()
        self.stdout.write(f'{client}')
