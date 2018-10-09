from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import User, Good


class GoodInLine(admin.StackedInline):
    model = Good
    extra = 1


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'login_times', 'create_time']
    inlines = [GoodInLine]


class GoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'price', 'viewtimes', 'create_time']


admin.site.register(User, UserAdmin)
admin.site.register(Good, GoodAdmin)

admin.site.site_header = u'365便民管理系统'
admin.site.site_title = u'365便民'
