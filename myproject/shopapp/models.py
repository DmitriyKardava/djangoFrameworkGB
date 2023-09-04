from django.db import models


class GetUndeletedManager(models.Manager): 
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class BaseModel(models.Model):
    objects = GetUndeletedManager()

    created = models.DateTimeField(auto_now_add=True, verbose_name="Created", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited", editable=False )
    deleted = models.BooleanField(default=False) 

    def delete(self, *args): 
        self.deleted = True 
        self.save()

    class Meta():
        abstract = True


class Client(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    registered_at = models.DateField(auto_now_add=True, blank=True)
    
    class Meta:
        ordering = ["name"]
        
    def __str__(self):
        return f'Name: {self.name}, email: {self.email}, phone: {self.phone}, registered: {self.registered_at}'
    
class Product(BaseModel):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    added_at = models.DateField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f'Name: {self.name}, price: {self.price}, count: {self.count}'


class Order(BaseModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, through='OrderItems')
    order_date = models.DateField(auto_now_add=True, blank=True)
    
    @property
    def order_price(self):
        result = 0
        order_items = OrderItems.objects.filter(order=self)
        for order_item  in order_items:
            result += order_item.items_count * order_item.product.price        
        return result
                       
    def __str__(self):
        return f'Client: {self.client.name}, OrderPrice: {self.order_price}'

class OrderItems(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    items_count = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['order', 'product'], name="uniq_product_in_order"),
            ]    

    def __str__(self):
        return f'Product: {self.product.name}, Count: {self.items_count}, Price: {self.product.price}'