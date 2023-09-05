from datetime import timedelta
from django.utils import timezone
from django.db.models.query import QuerySet
from django.views.generic.list import ListView
from shopapp.models import Order, OrderItems

class ClientProductsView(ListView):
    template_name = 'shopapp/client_products.html'
    paginate_by = 10
    def get_queryset(self):
        period = self.request.GET.get('period')
        match period:
            case 'per_week':
                orders = Order.objects.filter(client=1, order_date__gte = timezone.now().date() - timedelta(days=7))
            case 'per_month':
                orders = Order.objects.filter(client=1, order_date__gte = timezone.now().date() - timedelta(days=30))
            case 'per_year':
                orders = Order.objects.filter(client=1, order_date__gte = timezone.now().date() - timedelta(days=365))
            case _:
                orders = Order.objects.filter(client=1)      
        queryset = OrderItems.objects.filter(order__in=orders).order_by('product').distinct()
        
        return queryset
    