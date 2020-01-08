from rest_framework import serializers
from shop.models import DeliveryAddress, Product, Order, UserProfile, ManuFacturer, Category


class ProductListSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'model', 'image', 'price', 'sold', 'category', 'manufacturer']
