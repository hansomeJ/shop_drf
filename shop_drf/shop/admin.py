from django.contrib import admin

# Register your models here.
from shop.models import Product, Category, ManuFacturer, UserProfile, DeliveryAddress, Order, Notice
from django.contrib.auth.models import User


class MyAdminSite(admin.AdminSite):
    site_header = '篮球俱乐部物资管理系统'  # 此处设置页面显示标题
    site_title = '篮球俱乐部'  # 此处设置页面头部标题


admin.site.site_header = '篮球俱乐部物资管理系统'
admin.site.site_title = '篮球俱乐部'
# admin.site.index_title = '后台管理'
admin_site = MyAdminSite(name='management')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'mobile_phone', 'nickname', 'user', ]


admin.site.register(UserProfile, UserProfileAdmin)


class NoticeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', ]


admin.site.register(Notice, NoticeAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]


admin.site.register(Category, CategoryAdmin)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]


admin.site.register(ManuFacturer, ManufacturerAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'price', 'category', 'manufacturer', 'sold', ]
    list_editable = ['price', 'sold', 'category', ]


admin.site.register(Product, ProductAdmin)


class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'contact_person', 'contact_mobile_phone', 'delivery_address', ]


admin.site.register(DeliveryAddress, DeliveryAddressAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'user', ]


admin.site.register(Order, OrderAdmin)
