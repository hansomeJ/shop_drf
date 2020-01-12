# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-12 14:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200112_2207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '管理员', 'verbose_name_plural': '管理员'},
        ),
        migrations.AlterModelOptions(
            name='deliveryaddress',
            options={'verbose_name': '收货地址', 'verbose_name_plural': '收货地址'},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'verbose_name': '品牌', 'verbose_name_plural': '品牌'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': '订单', 'verbose_name_plural': '订单'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '物资', 'verbose_name_plural': '物资'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
    ]
