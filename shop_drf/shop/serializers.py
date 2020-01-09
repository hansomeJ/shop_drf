from rest_framework import serializers
from shop.models import DeliveryAddress, Product, Order, UserProfile, ManuFacturer, Category


class ManuFacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManuFacturer
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductListSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'model', 'image', 'price', 'sold', 'category', 'manufacturer']


class ProductRetrieveSerializer(serializers.ModelSerializer):
    manufacturer = ManuFacturerSerializer()
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ['id', 'model', 'image', 'price', 'sold', 'category', 'manufacturer', 'description']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'mobile_phone', 'nickname', 'description', 'icon', 'created', 'updated']
