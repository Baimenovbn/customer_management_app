from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    
    context = {'orders': orders, 'customers': customers,
    'total_customers': total_customers, 'total_orders': total_orders,
    'delivered': delivered, 'pending': pending}
    return render(request, 'accounts/index.html', context)

def products(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'accounts/products.html', context)
    
def customer(request, id):
    customer = Customer.objects.get(pk=id)
    orders = customer.order_set.all()
    total_orders = orders.count()

    context = {'customer': customer, 'orders': orders, 'total_orders': total_orders }
    return render(request, 'accounts/customer.html', context)

