from django.db import models
from uuid import uuid4

# Create your models here.

    
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    
    def __str__(self) -> str:
        return self.name
    
    def get_product_count(self):
        return self.products.count()
    
    class Meta:
        db_table = 'Category'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'Brand'
        managed = True
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
    
    
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False)
    name = models.CharField(max_length=100, )
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True, related_name='products')
    description = models.TextField()
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True, related_name='products')
    photo = models.ImageField(upload_to=f'photos/{category.name}/%Y/%m/%d/', null=True, blank=True, default=f'photos/{category}/ghost.png')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_date = models.DateField()
    color = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'Product'
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'