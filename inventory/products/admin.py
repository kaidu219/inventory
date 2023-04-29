from django.contrib import admin
from .models import Product, Category, Brand
from django.db.models import Count

# Register your models here.
@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand')
    list_filter = ('name', 'category', 'brand')
    


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'count_products')
    
    def count_products(self, obj):
        result = Product.objects.filter(category=obj).aggregate(Count('category'))
        return result['category__count']

    
@admin.register(Brand)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('name', 'count_products')
    
    def count_products(self, obj):
        result = Product.objects.filter(brand=obj).aggregate(Count('brand'))
        return result['brand__count']