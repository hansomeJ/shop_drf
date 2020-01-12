from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from rest_framework.routers import format_suffix_patterns

from shop.views import ProductList, ProductListByCategoryView, ProductListByCategoryManufacturerView, ProductRetrieve, \
    UserInfoView, CartListView, OrderListView
from shop import views

urlpatterns = [
    url(r'^product_list/', ProductList.as_view(), name='product_list'),
    url(r'^product_list_by_category/', ProductListByCategoryView.as_view(), name='product_list_by_category'),
    url(r'^product_list_by_category_manufacturer/', ProductListByCategoryManufacturerView.as_view(),
        name='product_list_by_category_manufacturer'),
    url(r'^product_retrieve/(?P<pk>[0-9]+)/', ProductRetrieve.as_view(), name='product_retrieve'),
    url(r'^user_info/', UserInfoView.as_view(), name='user_info'),
    url(r'^user_profile_ru/(?P<pk>[0-9]+)/', views.UserProfileView.as_view(), name='user_profile_ru'),
    url(r'^user_create/', views.UserCreateView.as_view(), name='user_create'),
    url(r'^delivery_address_lc/', views.DeliveryAddressLCView.as_view(), name='delivery_address_lc'),
    url(r'^delivery_address_rud/(?P<pk>[0-9]+)/', views.DeliveryAddressRUDView.as_view(), name='delivery_address_rud'),
    url(r'^cart_list/', views.CartListView.as_view(), name='cart_list'),
    url(r'^order_list/', views.OrderListView.as_view(), name='order_list'),
    url(r'^order_create/', views.OrderCreateView.as_view(), name='order_create'),
    url(r'^order_rud/(?P<pk>[0-9]+)/', views.OrderRetrieveUpdateDestroyView.as_view(), name='order_rud'),
    url(r'^notice/(?P<pk>[0-9]+)/', views.NoticeRetrieveView.as_view(), name='notice'),
    url(r'^notice/', views.NoticeListView.as_view(), name='notice'),

]
urlpatterns = format_suffix_patterns(urlpatterns)
