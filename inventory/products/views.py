from django.shortcuts import render
from rest_framework.response import Response
from .permissions import MyPermissions
from rest_framework.pagination import PageNumberPagination
# Create your views here.
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Product, Category, Brand
from .serializers import ProductSerializer, CategorySerializer, BrandSerializer, BrandCreateSerializer, BrandDetailViewSerializer, CategoryCreateSerializer, CategoryDetailViewSerializer

# Product
class ProductsView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(products, request)
        serializer = self.serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        category = Category.objects.get(name=data['category'])
        brand = Brand.objects.get(name=data['brand'])
        if category and brand:
            data['category'] = category.id
            data['brand'] = brand.id
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response('Вы ввели не сущетвующий бренд или категорию', serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
    

class ProductDetailView(APIView):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, id):
        data = request.data
        category = Category.objects.get(name=data['category'])
        brand = Brand.objects.get(name=data['brand'])
        product = Product.objects.get(id=id)
        if category and brand:
            data['category'] = category.id
            data['brand'] = brand.id
            serializer = ProductSerializer(product, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response('Вы ввели не сущетвующий бренд или категорию', serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        product = Product.objects.get(id=id)
        if product:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response('Товар не найден',status=status.HTTP_404_NOT_FOUND)
        
# Brand
class BrandAPIView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    create_serializer_class = BrandCreateSerializer
    
    def get(self, request, *args, **kwargs):
        queryset = Brand.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        brand = Brand.objects.filter(name=request.data['name'])
        if brand.exists():
            return Response(f"Бренд {request.data['name']} уже существует", status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
   
    
class BrandDetailAPIView(APIView):
    def get(self, request, name):
        brand = Brand.objects.get(name=name)
        serializer = BrandDetailViewSerializer(brand)
        return Response(serializer.data)
    
    def put(self, request, name):
        brand = Brand.objects.get(name=name)
        serializer = BrandCreateSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, name):
        brand = Brand.objects.get(name=name)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BrandListDetailAPIView(APIView):
    
    def get(self, request, name):
        try:
            brand = Brand.objects.get(name=name)
        except Brand.DoesNotExist:
            return Response({'error': f'Brand with name {name} does not exist'})
        
        products = Product.objects.filter(brand=brand)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
# Category
class CategoryAPIView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    create_serializer_class = CategoryCreateSerializer

    def get(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
 
    def post(self, request, *args, **kwargs):
        category = Category.objects.filter(name=request.data['name'])
        if category.exists():
            return Response(f"Категория {request.data['name']} уже существует", status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
   
    
class CategoryDetailAPIView(APIView):
    def get(self, request, name):
        category = Category.objects.get(name=name)
        serializer = CategoryDetailViewSerializer(category)
        return Response(serializer.data)
    
    def put(self, request, name):
        category = Category.objects.get(name=name)
        serializer = CategoryCreateSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name):
        category = Category.objects.get(name=name)
        if category:
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(f'Категории с таким названием нет', status=status.HTTP_404_NOT_FOUND)
            
class CategoryListDetailAPIView(APIView):
    permission_classes = [MyPermissions]
    def get(self, request, name):
        try:
            category = Category.objects.get(name=name)
        except Category.DoesNotExist:
            return Response({'error': f'Category with name {name} does not exist'})
        
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
          