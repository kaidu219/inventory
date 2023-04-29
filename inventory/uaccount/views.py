from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializers
from rest_framework.response import Response

# Create your views here.

class UserFavoriteList(APIView):
    def get(self, request):
        serializer = UserSerializers(request.user)
        return Response(serializer.data)
        
        
# class UserFavoriteList(APIView):
#     def get(self, request):
#         serializer = UserSerializers(request.user)
#         return Response(serializer.data)
    
    