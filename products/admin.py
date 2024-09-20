from django.contrib import admin
from .models import Product
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_filter = ['name']
    search_fields = ['name', 'price']