"""Product Serializers"""

from rest_framework import serializers

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


class ParentCategorySerializer(serializers.ModelSerializer):
    """Serializer for the ParentCategory model to handle data validation and transformation."""

    class Meta:
        """Meta class that defines model and fields for the ParentCategory serializer."""
        model = ParentCategory
        fields = ('name', 'description', 'image', 'slug')
        read_only_fields = ['slug']


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for the Category model to handle data validation and transformation."""
    parent_category = ParentCategorySerializer(read_only=True, many=True)

    class Meta:
        """Meta class that defines model and fields for the Category serializer."""
        model = Category
        fields = ("name", "parent_category", "description", "image", 'slug')
        read_only_fields = ['slug']


class SubCategorySerializer(serializers.ModelSerializer):
    """Serializer for the SubCategory model to handle data validation and transformation."""
    category = CategorySerializer(read_only=True, many=True)

    class Meta:
        """Meta class that defines model and fields for the SubCategory serializer."""
        model = SubCategory
        fields = ("name", "category", "description", "image")


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for the Product model to handle data validation and transformation."""

    class Meta:
        """Meta class that defines model and fields for the Product serializer."""
        models = Product
        fields = ["title", "description", "price", "stock"]
