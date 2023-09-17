from django.contrib import admin
from shopapp.models import Client, Product, Order

class ProductAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_filter = ['added_at', 'price']
    search_fields = ['desc']
    search_help_text = 'Поиск по полю Описание продукта (description)'
class ItemsInline(admin.TabularInline):
    model = Order.product.through
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        ItemsInline,
    ]

admin.site.register(Client)
admin.site.register(Product, ProductAdmin)

