from rest_framework import serializers
from .models import UserFavoriteProducts
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['favorites'] = UserFavoriteProductSerializers(instance.favorite.all(), many=True, context=self.context).data
        
        return context
    
class UserFavoriteProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserFavoriteProducts
        fields = '__all__'
        
    