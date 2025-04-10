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
        fields = ['name', 'description', 'image']


# class ParentCategorySerializer(serializers.ModelSerializer):
#     """Serializer for the ParentCategory model to handle data validation and transformation."""
#     image = serializers.SerializerMethodField()

#     class Meta:
#         """Meta class that defines model and fields for the ParentCategory serializer."""
#         model = ParentCategory
#         fields = ['name', 'description', 'image']

#     def get_image(self, obj):
#         """Method to retrieve image URL if available."""
#         request = self.context.get('request')
#         if obj.image and hasattr(obj.image, 'url'):
#             return request.build_absolute_uri(obj.image.url) if request else obj.image.url
#         return None


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for the Category model to handle data validation and transformation."""
    parent_category = ParentCategorySerializer(read_only=True, many=True)

    class Meta:
        """Meta class that defines model and fields for the Category serializer."""
        model = Category
        fields = ("name", "parent_category", "description", "image")


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
