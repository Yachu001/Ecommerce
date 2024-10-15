from django.shortcuts import render
from django.core.paginator import Paginator
from . models import Products

# Create your views here.
def Index(request):
    featured_product = Products.objects.order_by('id')[:4]
    latest_product = Products.objects.order_by('-id')[:4]
    context = {
        'fp': featured_product,
        'lp': latest_product
    }
    return render(request,'index.html',context)

def products_list(request):
    page= 1
    if request.GET:
        page = request.GET.get('page', 1)
    product_list = Products.objects.all()
    product_paginator = Paginator(product_list, 4)
    product_list= product_paginator.get_page(page)
    
    context = {'products': product_list}
    return render(request, 'products.html', context)

def product_details(request,pk):
    product = Products.objects.get(pk=pk)
    context ={
        'product':product
    }
    return render(request,'product_details.html',context)