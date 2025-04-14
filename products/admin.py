""" Admin configuration for products models """


from django.contrib import admin

from products.models import (
    ParentCategory,
    Category,
    SubCategory,
    Color,
    Size,
    Brand,
    Material,
    Product,
    ProductImages,
)


class ParentCategoryAdmin(admin.ModelAdmin):
    """Parent category admin model register"""
    list_display = ('name', 'description', 'image')
    search = ('name', )


admin.site.register(ParentCategory, ParentCategoryAdmin)


class CategoryAdmin(admin.ModelAdmin):
    """Category admin model register"""
    list_display = ('parent_category', 'name', 'description', 'image')
    search_fields = ('parent_category__name', 'name')


admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    """Subcategory admin model register"""
    list_display = ('category', 'name', 'description', 'image')
    search_fields = ('category__name', 'name')


admin.site.register(SubCategory, SubCategoryAdmin)


class ColorAdmin(admin.ModelAdmin):
    """Color admin model register"""
    list_display = ('name',)
    search_fields = ('name', )


admin.site.register(Color, ColorAdmin)


class SizeAdmin(admin.ModelAdmin):
    """Size admin model register"""
    list_display = ('name', )
    search_fields = ('name', )


admin.site.register(Size, SizeAdmin)


class BrandAdmin(admin.ModelAdmin):
    """Brand admin model register"""
    list_display = ('name', )
    search_fields = ('name', )


admin.site.register(Brand, BrandAdmin)


class MaterialAdmin(admin.ModelAdmin):
    """Material admin model register"""
    list_display = ('name', )


admin.site.register(Material, MaterialAdmin)

admin.site.register(Product)


class ProductImagesAdmin(admin.ModelAdmin):
    """Product Images admin model register"""
    list_display = ('product', 'image')
    search_fields = ('product__title',)


admin.site.register(ProductImages, ProductImagesAdmin)
