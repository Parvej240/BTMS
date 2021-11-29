from .models import Product, Order
from django.shortcuts import render


# Create your views here.


def productview(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
    else:
        order = {'get_cart_items': 0, 'get_cart_total': 0}

    if request.POST:
        search = request.POST['search']
        products = Product.objects.filter(name__contains=search)

    context = {'order': order, 'products': products}
    return render(request, 'product/list.html', context)
