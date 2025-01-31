from django.contrib import admin
from .models import Orders_item,Orders

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_filter=[
        "owner",
        "order_status",
    ]

    search_fields =(
        "owner",
        "id",
    )

admin.site.register(Orders,OrderAdmin)
admin.site.register(Orders_item)
