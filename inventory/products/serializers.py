from rest_framework import serializers
from .models import Product, Category, Brand

# product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['category'] = instance.category.name
        context['brand'] = instance.brand.name
        # context['name'] = instance.name
        return context



# category 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['count_kinds_products'] = instance.products.all().count()
        context['count_products'] = 0
        
        for i in instance.products.all():
            context['count_products'] += i.quantity
        return context
    
    
class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'   

class CategoryDetailViewSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['count_kinds_products'] = instance.products.all().count()
        context['count_products'] = 0
        
        for i in instance.products.all():
            context['count_products'] += i.quantity
        return context
    class Meta:
        model = Category
        fields = '__all__'
        
# Brand
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        
    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['count_kinds_products'] = instance.products.all().count()
        context['count_products'] = 0
        
        for i in instance.products.all():
            context['count_products'] += i.quantity
        return context
    
class BrandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        
class BrandDetailViewSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['count_kinds_products'] = instance.products.all().count()
        context['count_products'] = 0
        
        for i in instance.products.all():
            context['count_products'] += i.quantity
        return context
    class Meta:
        model = Brand
        fields = '__all__'