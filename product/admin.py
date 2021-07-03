from django.contrib import admin
from product.models import Product

class ProductAdmin(admin.ModelAdmin) :
    list_display = (
        "pnum",
        "pname",
        "price",
        "pdate",
        "psum",
        "bcate",
        "mcate",
        "image",
        "best",
        )
admin.site.register(Product,ProductAdmin)