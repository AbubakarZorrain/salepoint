from datetime import date, datetime

from django.db.models import Q
from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def purchases(request):
    if request.method=="POST":
        fromdate = request.POST.get('datafrom')
        todata = request.POST.get('name')
        if(todata !=''):
            result = Purchase.objects.all().filter(name = todata)
            return render(request, "salepointapp/aboutus.html", {'result':result})
        else:
            result = Purchase.objects.all().filter(Q(date=fromdate) | Q(name=todata))
            return render(request, "salepointapp/aboutus.html", {'result': result})

    data2 = Purchase.objects.all()
    context = {'data2':data2}
    return render(request, "salepointapp/aboutus.html",context)

def sales(request):
    if request.method=="POST":
        product = request.POST.get('productname')
        quantity = request.POST.get('quantity')
        remaining = request.POST.get('remaining')
        Product.objects.all().filter(name = product).update(quantity = remaining)
        q = Product(name = product)
        quant = q.quantity;
        result = Product.objects.all().filter(name = product)
        data = OrderItem.objects.all()
        context = {'result':result,'q':quant,'data':data}
        return render(request,'salepointapp/sales.html',context)
    else:
        data = sale.objects.all()
        q = Product.objects.filter(name='Second Product').values('quantity')
        quan = q.annotate(difference = F('quantity')-1)
        quant = quan
        context = {'q': quant,'data':data}
        return render(request,'salepointapp/sales.html',context)

def employee(request):
    employee = Employee.objects.all()
    context={'employee':employee}
    return render(request,'salepointapp/employee.html',context)
def products(request):
    form = ProductForm()
    product = Product.objects.all()
    context = {'product': product,'ProductForm':form}
    if request.method=="POST" and request.FILES['myfile']:
        try:
            productname = request.POST.get('productname')
            productquantity = request.POST.get('productquantity')
            productscheme = request.POST.get('productscheme')
            productrate = request.POST.get('productrate')
            productdiscountPercent = request.POST.get('productdiscountPercent')
            productdiscount = request.POST.get('productdiscount')
            productgst = request.POST.get('productgst')
            productvalue = request.POST.get('productvalue')
            product_image =  request.FILES['myfile']
            Product.objects.create(name=productname,quantity=productquantity,scheme=productscheme,rate=productrate,
                               discountPercent=productdiscountPercent,discount=productdiscount,gst=productgst,
                               value=productvalue,product_image=product_image)
            return render(request, 'salepointapp/products.html', context)
        except:
            return render(request, 'salepointapp/products.html', context)

    return render(request,'salepointapp/products.html',context)
def saleProduct(request):
    product = SaleProduct.objects.all()
    context = {'product': product}
    return render(request,'salepointapp/products.html',context)
def routes(request):
    routes = Routes.objects.all()
    context = {'routes': routes}
    return render(request,'salepointapp/routes.html',context)
def home(request):
    return render(request,'salepointapp/home.html')