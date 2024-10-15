from django.urls import path
from . views import Index, products_list, product_details
urlpatterns = [
    path('',Index, name='home'),
    path('products/',products_list, name='products'),
    path('product_details/<pk>',product_details, name='product_details'),
]