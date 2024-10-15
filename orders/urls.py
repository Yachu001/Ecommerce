from django.urls import path
from . views import Add_to_cart,Show_cart,Remove_cart_item,Cart_checkout,Orders_list

urlpatterns = [
    path('cart/',Show_cart , name='cart'),
    path('add_to_cart/',Add_to_cart,name='add_to_cart'),
    path('remove/<pk>',Remove_cart_item, name='remove'),
    path('checkout',Cart_checkout, name='checkout'),
    path('orders',Orders_list,name='orders'),
]