# coding: utf-8

from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from .models import *
from django import forms

from mptt.forms import TreeNodeChoiceField, TreeNodeMultipleChoiceField

class TitleInline(admin.TabularInline):
    model = Title

class SizeInline(admin.TabularInline):
    model = Size

class ObjectAdmin(admin.ModelAdmin):
    inlines = [
        TitleInline,
        SizeInline
    ]
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'material':
            field = TreeNodeChoiceField(queryset=Material.objects.all())
        else:
            field = super(ObjectAdmin,self).formfield_for_dbfield(
                                                  db_field,**kwargs)
        return field

admin.site.register(Title_type)
admin.site.register(Lang)
admin.site.register(Collection)
admin.site.register(Size_unit)
admin.site.register(Size_type)

admin.site.register(Title)
admin.site.register(Object, ObjectAdmin)


class MaterialAdmin(DjangoMpttAdmin):
    tree_auto_open = 0
    list_display = ('name',)
    ordering = ('name',)

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser


admin.site.register(Material, MaterialAdmin)



