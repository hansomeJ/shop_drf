from django.shortcuts import render

# Create your views here.
from shop.models import DeliveryAddress, Product, Order, UserProfile, ManuFacturer, Category
from shop.serializers import ProductListSerlizer, ProductRetrieveSerializer
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import permissions
from rest_framework.response import Response


class ProductList(generics.ListAPIView):
    """
    产品列表
    filter_backends : 筛选接口
    ordering_fields : 排序字段
    search_fields : 搜索字段
    """
    queryset = Product.objects.all()
    # permission_classes = (permissions.AllowAny)
    serializer_class = ProductListSerlizer
    filter_backends = (OrderingFilter, SearchFilter)
    # 排序字段
    ordering_fields = ('category', 'manufacturer', 'created', 'sold', 'stock',)
    # 搜索字段
    search_fields = ('model',)
    # 默认排序字段
    ordering = ('-id',)
    # 分页数量字段
    pagination_class = LimitOffsetPagination


class ProductListByCategoryView(generics.ListAPIView):
    serializer_class = ProductListSerlizer
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ('category', 'manufacturer', 'created', 'sold', 'price', 'stock')
    search_fields = ('description',)
    ordering = ('-id',)

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = Product.objects.filter(category=category)
        else:
            queryset = Product.objects.all()
        return queryset


class ProductListByCategoryManufacturerView(generics.ListAPIView):
    serializer_class = ProductListSerlizer
    filter_backends = (SearchFilter, OrderingFilter)
    ordering_fields = ('category', 'manufacturer', 'created', 'sold', 'price', 'stock')
    search_fields = ('description',)
    ordering = ('-id',)

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        manufacturer = self.request.query_params.get('manufacturer', None)
        if category and manufacturer is not None:
            queryset = Product.objects.filter(category=category, manufacturer=manufacturer)
        else:
            queryset = Product.objects.all()
        return queryset


class ProductRetrieve(generics.RetrieveAPIView):
    """
    商品详情
    """
    serializer_class = ProductRetrieveSerializer
    queryset = Product.objects.all()
