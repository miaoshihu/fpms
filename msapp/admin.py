from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-

from .models import Good, Need, City, Author
from django.utils.safestring import mark_safe


class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'enabled']
    model = City

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        extra_context['object_id'] = object_id
        print("object      id = " + object_id)
        extra_context['type'] = 'city'
        extra_context['publish_url'] = '/fps/publish'
        return super(CityAdmin, self).change_view(request, object_id,
                                                        extra_context=extra_context)

    class Media:
        js = [
            'js/csrf.js',
            'jquery/jquery.min.js',
        ]


class GoodInLine(admin.TabularInline):
    # can_delete = False
    can_delete = True

    def has_add_permission(self, request):
        return False

    def get_readonly_fields(self, request, obj=None):
        return ['name', 'status', 'price', 'create_time']

    model = Good
    extra = 1
    fields = ('name', 'status', 'price', 'create_time')
    # readonly_fields = ['name', 'status_type', 'price', 'create_time']


class NeedInLine(admin.TabularInline):

    # can_delete = False
    can_delete = True

    def has_add_permission(self, request):
        return False

    def get_readonly_fields(self, request, obj=None):
        return ['name', 'status', 'price', 'create_time']

    model = Need
    extra = 1
    fields = ('name', 'status', 'price', 'create_time')
    # readonly_fields = ['name', 'status_type', 'price', 'create_time']


class GoodAdmin(admin.ModelAdmin):

    # can_delete = False
    can_delete = True

    verbose_name = ""
    verbose_name_plural = ""

    list_display = ['id', 'name', 'price', "user_nickname", 'is_verify', 'get_status', 'create_time']
    readonly_fields = ['city', 'id', "user_nickname", 'name', 'price', 'short_desc', 'phone', 'image1', 'image2', 'show_image_1', 'show_image_2',
                       'descs', 'address', 'get_status',
                       'create_time', 'time_stamp', 'author']
    list_filter = ('city__name', 'status')

    model = Good

#    def has_add_permission(self, request):
#        return False
#
#    def has_delete_permission(self, request, obj=None):
#        return False

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        extra_context['object_id'] = object_id
        extra_context['type'] = 'good'
        extra_context['publish_url'] = '/fps/publish'
        return super(GoodAdmin, self).change_view(request, object_id,
                                                        extra_context=extra_context)

    def show_image_1(self, obj):
        try:
            img = mark_safe('<img src="%s" width="250px" />' % (obj.image1,))
        except Exception as e:
            img = ''
        return img

    def show_image_2(self, obj):
        try:
            img = mark_safe('<img src="%s" width="250px" />' % (obj.image2,))
        except Exception as e:
            img = ''
        return img

    show_image_1.short_description = 'image1'
    show_image_1.allow_tags = True

    show_image_2.short_description = 'image2'
    show_image_2.allow_tags = True

    class Media:
        js = [
            'js/csrf.js',
            'jquery/jquery.min.js',
        ]


class NeedAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'price', 'author', "user_nickname", 'address', 'is_verify', 'get_status', 'create_time']
    readonly_fields = ["user_nickname", 'name', 'price', 'phone', 'address',
                       'descs',
                       'create_time', 'city', 'time_stamp', 'author']
    list_filter = ('city__name',)
    model = Need

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        extra_context['object_id'] = object_id
        extra_context['type'] = 'need'
        extra_context['publish_url'] = '/fps/publish'
        return super(NeedAdmin, self).change_view(request, object_id,
                                                        extra_context=extra_context)

    class Media:
        js = [
            'js/csrf.js',
            'jquery/jquery.min.js',
        ]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', "point", 'descs', 'town', 'address', 'status', 'is_verify', 'phone', 'create_time', ]
    readonly_fields = ['id', "nickname", 'town', 'address', 'phone', 'create_time', 'time_stamp']
    list_filter = ('status',)
    model = Author
    inlines = [GoodInLine, NeedInLine]

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        extra_context['object_id'] = object_id
        extra_context['type'] = 'author'
        extra_context['publish_url'] = '/fps/publish'
        return super(AuthorAdmin, self).change_view(request, object_id,
                                                        extra_context=extra_context)

    class Media:
        js = [
            'js/csrf.js',
            'jquery/jquery.min.js',
        ]


admin.site.register(City, CityAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(Need, NeedAdmin)
admin.site.register(Author, AuthorAdmin)

admin.site.site_header = u'本地旧货header'
admin.site.site_title = u'本地旧货title'
