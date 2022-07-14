from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from .models import Category, Customer, Product, SubCategory
from .serializer import CategorySerializer, CustomerSerializer, ProductSerializer, SubCategorySerializer


# category
class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# customer
class CustomerAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# product
class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# sub_category
class SubCategoryAPIView(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
