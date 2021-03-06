# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-12 14:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200112_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, verbose_name='类别名'),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='deliveryaddress',
            name='contact_mobile_phone',
            field=models.CharField(max_length=200, verbose_name='收货人电话'),
        ),
        migrations.AlterField(
            model_name='deliveryaddress',
            name='contact_person',
            field=models.CharField(max_length=200, verbose_name='收货人姓名'),
        ),
        migrations.AlterField(
            model_name='deliveryaddress',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='deliveryaddress',
            name='delivery_address',
            field=models.TextField(verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='deliveryaddress',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='deliveryaddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_address_of', to=settings.AUTH_USER_MODEL, verbose_name='所有者'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='description',
            field=models.TextField(verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='logo',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='manufacturer/uploads/%Y/%m/%d/', verbose_name='logo'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(max_length=200, verbose_name='品牌名'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_address', to='shop.DeliveryAddress', verbose_name='收货地址'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_product', to='shop.Product', verbose_name='物资'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='order',
            name='remark',
            field=models.TextField(blank=True, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('0', '正在租借'), ('1', '已归还')], default='0', max_length=2, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_of', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_in', to='shop.Category', verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(max_length=200, upload_to='product/uploads/%Y/%m/%d/', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_of', to='shop.ManuFacturer', verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.CharField(max_length=200, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sold',
            field=models.PositiveIntegerField(default=0, verbose_name='销量'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='delivery_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_delivery_address', to='shop.DeliveryAddress', verbose_name='收货地址'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='icon',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='user/uploads/%Y/%m/%d/', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile_phone',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_of', to=settings.AUTH_USER_MODEL, verbose_name='账号'),
        ),
    ]
