from django.db import models
from customers.models import Customer
from products.models  import Products

# Create your models here.
class Orders(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,"LIVE"),(DELETE,"DELETE"))
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICES = ((ORDER_CONFIRMED,'ORDER_CONFIRMED'),
                      (ORDER_PROCESSED,'ORDER_PROCESSED'),
                      (ORDER_DELIVERED,'ORDER_DELIVERED'),
                      (ORDER_REJECTED,'ORDER_REJECTED'),)
    owner = models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True, related_name='orders')
    total_price = models.FloatField(default=0)
    order_status = models.IntegerField(choices=STATUS_CHOICES, default= CART_STAGE)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default= LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "order-{}-{}".format(self.id, self.owner.name)

class Orders_item(models.Model):
    product = models.ForeignKey(Products,on_delete=models.SET_NULL, null=True, related_name= 'added_order')
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Orders,on_delete=models.CASCADE ,related_name='added_items')