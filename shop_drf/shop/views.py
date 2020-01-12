from django.shortcuts import render

# Create your views here.
from shop.models import DeliveryAddress, Product, Order, UserProfile, ManuFacturer, Category
from shop.serializers import ProductListSerlizer, ProductRetrieveSerializer, UserInfoSerializer, UserProfileSerializer, \
    UserSerializer, DeliveryAddressSerializer, OrderListSerializer, OrderCreateSerializer, OrderSerializer
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

import json

import datetime

import logging

LOG_FILENAME = 'shop.log'

logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)


# logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)

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


class UserInfoView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        user = self.request.user
        serializer = UserInfoSerializer(user)
        return Response(serializer.data)


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # queryset = UserProfile.objects.all()
    def get_object(self):
        user = self.request.user
        obj = UserProfile.objects.get(user=user)
        return obj


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class DeliveryAddressLCView(generics.ListCreateAPIView):
    serializer_class = DeliveryAddressSerializer

    # 获取多个对象
    def get_queryset(self):
        user = self.request.user
        queryset = DeliveryAddress.objects.filter(user=user)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        s = serializer.save(user=user)
        print(user.profile_of)
        profile = user.profile_of
        profile.delivery_address = s
        profile.save()


class DeliveryAddressRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeliveryAddressSerializer

    # 获取一个对象
    def get_object(self):
        user = self.request.user
        # obj = DeliveryAddress.objects.get(user=user)
        try:
            obj = DeliveryAddress.objects.get(id=self.kwargs['pk'], user=user)
        except Exception as e:
            raise NotFound('not found')
        return obj


class CartListView(generics.ListAPIView):
    serializer_class = OrderListSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(user=user, status='0')
        return queryset


class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(user=user, status__in=['1', '2', '3', '4'])
        return queryset


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        product = serializer.validated_data.get('product')
        serializer.save(user=user, price=product.price, address=self.request.user.profile_of.delivery_address)
        # logging.debug('this is debug')
        # logging.info('this is critical %s','added')
        logging.info('user %d cart changed, product %d related. Time is %s.', user.id, product.id,
                     str(datetime.datetime.now()))


class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer

    def get_object(self):
        user = self.request.user
        obj = Order.objects.get(user=user, id=self.kwargs['pk'])
        return obj

    def perform_update(self, serializer):
        user = self.request.user
        s = serializer.save(user=user, status='1')
