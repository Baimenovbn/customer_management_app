from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import *
from .filters import OrderFilter


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

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer': customer, 'orders': orders, 
    'total_orders': total_orders, 'myFilter': myFilter}
    return render(request, 'accounts/customer.html', context)


def createOrder(request, id):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=8)
    customer = Customer.objects.get(id=id)
    formSet = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == 'POST':
        formSet = OrderFormSet(request.POST, instance=customer)
        if formSet.is_valid:
            formSet.save()
            return redirect('/')
            
    context = {'formSet': formSet}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid:
            form.save()
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, id):
    order = Order.objects.get(id=id)

    if request.method == 'POST':
        order.delete()
        return redirect('/')
    
    item = order.product
    context = {'item': item}
    return render(request, 'accounts/delete.html', context)
