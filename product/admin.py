from .models import Order, OrderItem, Product, ShippingAddress
from django.contrib import admin

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
