from django.shortcuts import render, redirect
from products.models import Products
from .models import Orders, Orders_item
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def Show_cart(request):
    user = request.user
    customer = user.customer_profile
    cart_obj, created = Orders.objects.get_or_create(
        owner=customer,
        order_status=Orders.CART_STAGE
    )
    context = {'cart': cart_obj}
    return render(request, 'cart.html', context)

@login_required(login_url='customer')
def Add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')
        cart_obj,created = Orders.objects.get_or_create(
            owner=customer,
            order_status=Orders.CART_STAGE
        )
        product = Products.objects.get(pk=product_id)
        ordered_item,created = Orders_item.objects.get_or_create(
            product=product,
            owner=cart_obj,
        )
        if created:
            ordered_item.quantity=quantity
            ordered_item.save()
        else:
            ordered_item.quantity = ordered_item.quantity +quantity
            ordered_item.save() 
    return redirect('cart')

def Remove_cart_item(request,pk):
    item = Orders_item.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')


def Cart_checkout(request):
    if request.POST:
        try:
            user = request.user
            customer = user.customer_profile
            total = float(request.POST.get('total'))
            order_obj = Orders.objects.get(
                        owner=customer,
                        order_status=Orders.CART_STAGE
                    )
            if order_obj:
                order_obj.order_status = Orders.ORDER_CONFIRMED
                order_obj.total_price = total
                order_obj.save()
                status_message = "Order Processed successfully"
                messages.success(request,status_message)
            else:
                status_message = "Unable to Proceed"
                messages.error(request,status_message)
        except Exception as e:
            status_message = "Unable to Proceed"
            messages.error(request,status_message)
    return redirect('cart')


@login_required(login_url='customer')
def Orders_list(request):
    user = request.user
    customer = user.customer_profile
    all_orders = Orders.objects.filter(owner=customer).exclude(order_status=Orders.CART_STAGE)
    context={
        'orders':all_orders
    }
    return render(request,'orders.html',context)
