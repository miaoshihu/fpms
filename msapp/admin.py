from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import User, Good, Need, City


class GoodInLine(admin.StackedInline):
    model = Good
    extra = 1


class NeedInLine(admin.StackedInline):
    model = Need
    extra = 1


class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'enabled']


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'login_times', 'create_time', 'enabled', 'white']
    readonly_fields = ['nickname', 'icon', 'desc', 'create_time', 'login_times']
    list_editable = ['enabled']
    inlines = [GoodInLine, NeedInLine]

    list_filter = ('enabled', 'white', 'city')


class GoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'status', 'short_desc', 'view_times', 'create_time']
    readonly_fields = ['user', 'name', 'price', 'short_desc', 'phone', 'image1', 'image2', 'image3', 'desc', 'address',
                       'view_times', 'create_time', 'last_modify_time', 'city']


class NeedAdmin(admin.ModelAdmin):
    list_display = ['name', 'price_min', 'price_max', 'status', 'short_desc', 'view_times', 'create_time']
    readonly_fields = ['user', 'name', 'price_min', 'price_max', 'phone', 'image1', 'address', 'desc', 'short_desc',
                       'view_times', 'create_time', 'last_modify_time', 'city']


admin.site.register(User, UserAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(Need, NeedAdmin)
admin.site.register(City, CityAdmin)

admin.site.site_header = u'本地旧货header'
admin.site.site_title = u'本地旧货title'
