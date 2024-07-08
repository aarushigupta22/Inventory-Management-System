from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product,Order
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='user-login')
def index(request):
    order = Order.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'order':order,
        'form': form,
    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.filter(is_superuser=False)
    context = {
        'workers':workers
    }
    return render(request, 'dashboard/staff.html',context)

@login_required(login_url='user-login')
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers':workers
    }
    return render(request, 'dashboard/staff_detail.html',context)

@login_required(login_url='user-login')
def product(request):
    #items = Product.objects.all(): this is using ORM method
    items = Product.objects.raw('SELECT * FROM dashboard_product')

    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form=ProductForm()
    context={
        'items':items,
        'form':form
    }
    return render(request, 'dashboard/product.html', context)


@login_required(login_url='user-login')
#@allowed_users(allowed_roles=['Admin'])
def product_delete(request, pk): #pk:primary key of the item i want to get
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    context = {
        'item': item
    }
    return render(request, 'dashboard/products_delete.html', context)

@login_required(login_url='user-login')
#@allowed_users(allowed_roles=['Admin'])
def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/products_edit.html', context)


@login_required(login_url='user-login')
def order(request):
    orders = Order.objects.all()
    context={
        'orders':orders,
    }
    return render(request, 'dashboard/order.html' , context)