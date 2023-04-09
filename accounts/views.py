from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from .forms import OrderForm
from django.forms import inlineformset_factory
# Create your views here.

#Home function

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = Order.objects.all().count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers,'total_customers': total_customers,'total_orders': total_orders, 'delivered': delivered,'pending': pending}


    return render(request, 'accounts/dashboard.html', context)


#def Products, return the list of products in the home page

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

#loads the customers of the DB to the home page

def customer(request,pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    orders_count = orders.count()

    context = {'customer': customer, 'orders': orders, 'orders_count': orders_count}
    return render(request, 'accounts/customers.html',context)

#re-direct to the form page, this handle the creation of orders and then send it to the DB


def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'))
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(instance=customer)
    #form = OrderForm(initial={'customer' : customer})
    if request.method == 'POST':

        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}
    return render(request, 'accounts/order_form.html', context)

# same as createOrder, but this just update existing orders

def updateOrder(request,pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

# same as update but this delete orders

def deleteOrder (request, pk):

    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)