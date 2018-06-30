from django.contrib import admin

# Register your models here.
from .models import Product
#
class ProductAdmin(admin.ModelAdmin):
    

    class Meta:
        model = Product

admin.site.register(Product)