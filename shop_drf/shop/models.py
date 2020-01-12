from django.db import models

# Create your models here.
from django.utils.six import python_2_unicode_compatible

from django.conf import settings


# 与python2兼容
@python_2_unicode_compatible
class Category(models.Model):
    """
    物资类别：篮球，球衣，球鞋，场地
    """
    name = models.CharField(max_length=200, verbose_name='类别名')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '管理员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class ManuFacturer(models.Model):
    """
    品牌
    """
    name = models.CharField(max_length=200, verbose_name='品牌名')
    description = models.TextField(verbose_name='描述')
    logo = models.ImageField(blank=True, null=True, max_length=200, upload_to='manufacturer/uploads/%Y/%m/%d/',
                             verbose_name='logo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Product(models.Model):
    """
    物资
    """
    model = models.CharField(max_length=200, verbose_name='名字')
    description = models.TextField(verbose_name='描述')
    image = models.ImageField(max_length=200, upload_to='product/uploads/%Y/%m/%d/', verbose_name='图片')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='价格')
    sold = models.PositiveIntegerField(default=0, verbose_name='销量')
    category = models.ForeignKey(Category, related_name='product_in', on_delete=models.CASCADE, verbose_name='类别')
    manufacturer = models.ForeignKey(ManuFacturer, related_name='product_of', on_delete=models.CASCADE,
                                     verbose_name='品牌')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '物资'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.model


@python_2_unicode_compatible
class DeliveryAddress(models.Model):
    """
    收货地址
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='delivery_address_of',
                             verbose_name='所有者')
    contact_person = models.CharField(max_length=200, verbose_name='收货人姓名')
    contact_mobile_phone = models.CharField(max_length=200, verbose_name='收货人电话')
    delivery_address = models.TextField(verbose_name='地址')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '收货地址'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.delivery_address


@python_2_unicode_compatible
class UserProfile(models.Model):
    """
    用户信息
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile_of',
                                verbose_name='账号')
    mobile_phone = models.CharField(blank=True, null=True, max_length=200, verbose_name='电话')
    nickname = models.CharField(blank=True, null=True, max_length=200, verbose_name='昵称')
    description = models.TextField(blank=True, null=True, verbose_name='简介')
    icon = models.ImageField(blank=True, null=True, max_length=200, upload_to='user/uploads/%Y/%m/%d/',
                             verbose_name='头像')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    delivery_address = models.ForeignKey(DeliveryAddress, related_name='user_delivery_address',
                                         on_delete=models.CASCADE, blank=True, null=True, verbose_name='收货地址')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


@python_2_unicode_compatible
class Order(models.Model):
    """
    订单
    """

    STATUS_CHOISE = (
        ('0', '正在租借'),
        ('1', '已归还'),
    )
    status = models.CharField(choices=STATUS_CHOISE, default='0', max_length=2, verbose_name='状态')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_of',
                             verbose_name='用户')
    remark = models.TextField(blank=True, null=True, verbose_name='备注')
    product = models.ForeignKey(Product, related_name='order_product', on_delete=models.CASCADE, verbose_name='物资')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='价格')
    quantity = models.PositiveIntegerField(default=1, verbose_name='数量')
    address = models.ForeignKey(DeliveryAddress, related_name='order_address', on_delete=models.CASCADE,
                                verbose_name='收货地址')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'order of %d' % (self.user.id)


@python_2_unicode_compatible
class Notice(models.Model):
    """
    公告表
    """
    title = models.CharField(max_length=200, verbose_name='公告标题')
    content = models.TextField(verbose_name='公告内容')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notice_of',
                             verbose_name='发布者')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '公告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
