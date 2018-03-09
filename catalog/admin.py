from django.contrib import admin
from . models import *


class CategoryIndexImgInline(admin.TabularInline):
    model = CategoryIndexImg
    extra = 1


class CategoryInnerImgInline(admin.TabularInline):
    model = CategoryInnerImg
    extra = 1


class CategoryCatalogImgInline(admin.TabularInline):
    model = CategoryCatalogImg
    extra = 1


class CategoryCatalogTextInline(admin.TabularInline):
    model = CategoryCatalogText
    extra = 1


class CategoryConsImgInline(admin.TabularInline):
    model = CategoryConsImg
    extra = 1


class CategoryConsTextInline(admin.TabularInline):
    model = CategoryConsText
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]
    inlines = [CategoryIndexImgInline, CategoryInnerImgInline, CategoryCatalogImgInline,
               CategoryCatalogTextInline, CategoryConsImgInline, CategoryConsTextInline]

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class ProductImgAdmin(admin.TabularInline):
    model = ProductImg
    extra = 2
    exclude = ['type']


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImgAdmin]
    exclude = ['type']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)