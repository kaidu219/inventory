from django.db import models
import uuid
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class UserFavoriteProducts(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, null=False, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='favorite')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='favorite')
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.user} favorite {self.product}'