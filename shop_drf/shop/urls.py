from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from rest_framework.routers import format_suffix_patterns

from shop.views import ProductList, ProductListByCategoryView, ProductListByCategoryManufacturerView,ProductRetrieve

urlpatterns = [
    url(r'^product_list/', ProductList.as_view(), name='product_list'),
    url(r'^product_list_by_category/', ProductListByCategoryView.as_view(), name='product_list_by_category'),
    url(r'^product_list_by_category_manufacturer/', ProductListByCategoryManufacturerView.as_view(),
        name='product_list_by_category_manufacturer'),
    url(r'^product_retrieve/(?P<pk>[0-9]+)/', ProductRetrieve.as_view(), name='product_retrieve'),

]
urlpatterns = format_suffix_patterns(urlpatterns)
