from django.contrib import admin

from order.models import Order
from order.models import Buy
from order.models import Recommend

class OrderAdmin(admin.ModelAdmin) :
    list_display = (
        "onum",
        "prod_num",
        "order_id",
        "quan",
        )
admin.site.register(Order,OrderAdmin)

class BuyAdmin(admin.ModelAdmin) :
    list_display = (
        "bnum",
        "member",
        "pnum",
        "pname",
        "price",
        "quan",
        "pay"
        )
admin.site.register(Buy,BuyAdmin)

class RecommendAdmin(admin.ModelAdmin):
    list_display = (
        "member",
        "product"
        )
admin.site.register(Recommend,RecommendAdmin)