from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-

from .models import Good, Need, City


class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'enabled']


class GoodInLine(admin.StackedInline):
    model = Good
    extra = 1


class NeedInLine(admin.StackedInline):
    model = Need
    extra = 1


class GoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'status', 'short_desc', 'create_time']
    # readonly_fields = ['user_id', "user_nickname", 'name', 'price', 'short_desc', 'phone', 'image1', 'image2', 'image3',
    #                    'desc', 'address',
    #                    'create_time', 'city']

    model = Good

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        extra_context['object_id'] = object_id
        extra_context['publish_url'] = '/fps/good/publish'
        return super(GoodAdmin, self).change_view(request, object_id,
                                                        extra_context=extra_context)
    class Media:
        js = [
            'js/csrf.js',
            'jquery/jquery.min.js',
        ]


class NeedAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'status', 'create_time']
    # readonly_fields = ['user_id', "user_nickname", 'name', 'price', 'phone', 'address',
    #                    'desc',
    #                    'create_time', 'city']
    model = Need

    class Media:
        js = [
            'js/csrf.js',
            'jquery/jquery.min.js',
        ]


admin.site.register(City, CityAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(Need, NeedAdmin)

admin.site.site_header = u'本地旧货header'
admin.site.site_title = u'本地旧货title'
