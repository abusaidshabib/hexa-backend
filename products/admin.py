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
    list_display = ('name', 'hex_code')
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


class ProductAdmin(admin.ModelAdmin):
    """Product admin model register"""

    list_display = ('title', 'description', 'price', 'subcategory_display', 'color_display', 'size_display',
                    'brand_display', 'material_display', 'stock', 'active', 'manufacturer', 'featured')
    search_fields = ('title', 'subcategory__name', 'color__name',
                     'size__name', 'brand__name', 'material__name')

    def subcategory_display(self, obj):
        """Display subcategories of a product"""
        return ", ".join([subcategory.name for subcategory in obj.subcategory.all()])
    subcategory_display.short_description = 'Subcategories'

    def color_display(self, obj):
        """Display colors of a product"""
        return ", ".join([color.name for color in obj.color.all()])
    color_display.short_description = 'Colors'

    def size_display(self, obj):
        """Display sizes of a product"""
        return ", ".join([size.name for size in obj.size.all()])
    size_display.short_description = 'Sizes'

    def brand_display(self, obj):
        """Display brands of a product"""
        return ", ".join([brand.name for brand in obj.brand.all()])
    brand_display.short_description = 'Brands'

    def material_display(self, obj):
        """Display materials of a product"""
        return ", ".join([material.name for material in obj.material.all()])
    material_display.short_description = 'Materials'


admin.site.register(Product, ProductAdmin)


class ProductImagesAdmin(admin.ModelAdmin):
    """Product Images admin model register"""
    list_display = ('product', 'image', 'thumbnail')
    search_fields = ('product__title',)


admin.site.register(ProductImages, ProductImagesAdmin)
