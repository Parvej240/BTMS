from django.urls.conf import path
from .views import *

urlpatterns = [
    path('cart', cart_summery, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('update-item/', updateItem, name='update-item'),
    path('process_order/', processOrder, name='process_order'),
    path('purchase_history/', purchase_history, name='purchase_history'),
]
