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


class SubCategorySerializer(serializers.ModelSerializer):
    """Serializer for the SubCategory model to handle data validation and transformation."""
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),  # pylint: disable=no-member
        slug_field='slug',  # Look up by the slug of Category
        required=True
    )

    class Meta:
        """Meta class that defines model and fields for the SubCategory serializer."""
        model = SubCategory
        fields = ("name", "category", "description", "image", 'slug')

    def validate_category(self, value):
        """Validate that the category belongs to the same parent category as the instance."""
        if self.instance and value != self.instance.category:
            raise serializers.ValidationError(
                "The category must belong to the same parent category."
            )
        return value


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for the Category model to handle data validation and transformation."""

    parent_category = serializers.SlugRelatedField(
        queryset=ParentCategory.objects.all(),  # pylint: disable=no-member
        slug_field='slug',  # Look up by the slug of ParentCategory
        required=True,
        write_only=True
    )

    subcategories = SubCategorySerializer(
        many=True, required=False, read_only=True)  # pylint: disable=no-member

    class Meta:
        """Meta class that defines model and fields for the Category serializer."""
        model = Category
        fields = ("name", "description", "image", 'slug',
                  "parent_category", "subcategories")
        read_only_fields = ['slug']


class ParentCategorySerializer(serializers.ModelSerializer):
    """Serializer for the ParentCategory model to handle data validation and transformation."""

    categories = CategorySerializer(
        many=True, required=False, read_only=True)  # pylint: disable=no-member

    class Meta:
        """Meta class that defines model and fields for the ParentCategory serializer."""
        model = ParentCategory
        fields = ('name', 'description', 'image', 'slug', 'categories')
        read_only_fields = ['slug']




class ProductSerializer(serializers.ModelSerializer):
    """Serializer for the Product model to handle data validation and transformation."""

    class Meta:
        """Meta class that defines model and fields for the Product serializer."""
        models = Product
        fields = ["title", "description", "price", "stock"]
