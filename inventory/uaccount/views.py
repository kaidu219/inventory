from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializers
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

# Create your views here.

class UserFavoriteList(APIView):
    def get(self, request):
        serializer = UserSerializers(request.user)
        return Response(serializer.data)
        
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(email=request.data['email'])
        if user.exists():
            return Response(f'Аккаунт с emailom {user} уже существует, попытайтесь вспомнить пароль или используйте другой email.')
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        
       
# class UserFavoriteList(APIView):
#     def get(self, request):
#         serializer = UserSerializers(request.user)
#         return Response(serializer.data)
    
    