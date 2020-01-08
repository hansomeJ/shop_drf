from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from rest_framework.routers import format_suffix_patterns

from shop.views import ProductList

urlpatterns = [
    url(r'^product/', ProductList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)