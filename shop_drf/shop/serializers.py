from rest_framework import serializers
from shop.models import DeliveryAddress, Product, Order, UserProfile, ManuFacturer, Category, Notice
from django.contrib.auth.models import User


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
        fields = ['id', 'user', 'mobile_phone', 'nickname', 'description', 'icon', 'created', 'updated']
        read_only_fields = ['user']


class UserInfoSerializer(serializers.ModelSerializer):
    profile_of = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'profile_of']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        user_profile = UserProfile(user=user)
        user_profile.save()
        return user


class DeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        fields = ['id', 'user', 'contact_mobile_phone', 'contact_person', 'delivery_address', 'created', 'updated']
        read_only_fields = ['user']


class OrderListSerializer(serializers.ModelSerializer):
    product = ProductListSerlizer()
    address = DeliveryAddressSerializer()

    class Meta:
        model = Order
        fields = ['id', 'user', 'product', 'price', 'quantity', 'created', 'updated', 'remark', 'address', 'status']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', ]


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'product', 'price', 'quantity', 'created', 'updated', 'remark', 'address', 'status']
        read_only_fields = ['user', 'price', 'address', 'status']


class NoticeListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Notice
        fields = ['id', 'title', 'user', ]
        read_only_fields = ['id', 'title', 'user', ]


class NoticeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Notice
        fields = ['id', 'title', 'content', 'user', 'created', 'updated']
        read_only_fields = ['id', 'title', 'user', 'created', 'updated']
