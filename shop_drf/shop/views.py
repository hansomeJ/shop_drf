from django.shortcuts import render

# Create your views here.
from shop.models import DeliveryAddress, Product, Order, UserProfile, ManuFacturer, Category
from shop.serializers import ProductListSerlizer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    # permission_classes = (permissions.AllowAny)
    serializer_class = ProductListSerlizer
