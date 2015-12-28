# -*- coding: utf-8 -*-


from django.db import models

from mptt.models import TreeForeignKey
import mptt

## Вспомагательные атрибуты

# Название


class Title_type(models.Model):
    title_type = models.CharField(u"Тип назви", max_length=50)

    class Meta:
        verbose_name = u'Тип назви'
        verbose_name_plural = u'Тип назви'

    def __unicode__(self):
        return self.title_type


class Lang(models.Model):
    lang = models.CharField(u"Мова", max_length=50)

    class Meta:
        verbose_name = u'Мова'
        verbose_name_plural = u'Мова'

    def __unicode__(self):
        return self.lang


# Розміри


class Size_type(models.Model):
    size_type = models.CharField(u"Тип виміру", max_length=50)

    class Meta:
        verbose_name = u'Тип виміру'
        verbose_name_plural = u'Тип виміру'

    def __unicode__(self):
        return self.size_type

class Size_unit(models.Model):
    size_unit = models.CharField(u"Одиниці виміру", max_length=50)

    class Meta:
        verbose_name = u'Одиниці виміру'
        verbose_name_plural = u'Одиниці виміру'

    def __unicode__(self):
        return self.size_unit

## Основные атрибуты предметов
## Класс коллекция
class Collection(models.Model):
    collection = models.CharField(u"Колекція", max_length=50)

    class Meta:
        verbose_name = u'Колекція'
        verbose_name_plural = u'Колекція'

    def __unicode__(self):
        return self.collection

class Material(models.Model):
    class Meta:
        verbose_name_plural = u'Матеріал'
        app_label = 'catalog'

    name = models.CharField(max_length=50, blank=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return self.name or ''


mptt.register(Material)

# Клас Название - язык названия + тип названия + название


class Object(models.Model):
    collections = models.ManyToManyField(Collection, verbose_name=u'Колекція')
    fragment = models.BooleanField(verbose_name="Є фрагментом", default=False)
    compounds_amount = models.DecimalField(verbose_name="Кількість фрагментів", default=1, decimal_places=0, max_digits=2)
    material = models.ForeignKey(Material, default='', verbose_name="Матеріал")
    class Meta:
        verbose_name = u'Предмет'
        verbose_name_plural = u'Предмет'

    def __str__(self):
        return 'Предмет № <{}> '.format(self.pk)


class Title(models.Model):
    title_type = models.ForeignKey(Title_type, verbose_name=u'Тип')
    title_lang = models.ForeignKey(Lang, verbose_name=u'Мова')
    title = models.CharField(u"Назва", max_length=50)
    object_id = models.ForeignKey(Object, verbose_name=u'Предмет')

    class Meta:
        verbose_name = u'Назва'
        verbose_name_plural = u'Назва'

    def __unicode__(self):
        return self.title

class Size(models.Model):
    size_type = models.ForeignKey(Size_type, verbose_name=u'Тип виміру')
    size_unit = models.ForeignKey(Size_unit, verbose_name=u'Одиниці виміру')
    size = models.FloatField(verbose_name=u'Значення')
    object_id = models.ForeignKey(Object, verbose_name=u'Предмет')

    class Meta:
        verbose_name = u'Назва'
        verbose_name_plural = u'Назва'

    def __unicode__(self):
        return self.size_type.size_type


class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category')

class Category(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True,
                                              related_name='children')

    class Meta:
        ordering = ('tree_id','level')
    def __unicode__(self):
        return self.title

mptt.register(Category, order_insertion_by=['title'])
