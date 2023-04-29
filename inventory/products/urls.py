from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .yasg import urlpatterns as doc_url

urlpatterns = [
    path('products/', ProductsView.as_view()),
    path('products/<str:id>', ProductDetailView.as_view()),
    
    path('brand/', BrandAPIView.as_view()),
    path('brandlist/<str:name>', BrandListDetailAPIView.as_view()),
    path('brand/<str:name>', BrandDetailAPIView.as_view()),
    
    path('category/', CategoryAPIView.as_view()),
    path('category/<str:name>', CategoryDetailAPIView.as_view()),
    path('categorylist/<str:name>', CategoryListDetailAPIView.as_view()),
]
urlpatterns += doc_url