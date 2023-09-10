from datetime import timedelta
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from shopapp.models import Order, OrderItems, Product
from shopapp.forms import ProductForm

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
        queryset = OrderItems.objects.filter(order__in=orders).order_by('created').distinct()
        
        return queryset
    
class ProductView(ListView):
    model = Product
    template_name = 'shopapp/products.html'
    paginate_by = 10
    
class ProductDetailView(UpdateView):
    template_name = "shopapp/product_detail.html"
    form_class = ProductForm
    success_url = "/product/"
    model = Product
