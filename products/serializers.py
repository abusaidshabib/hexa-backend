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


class ColorSerializer(serializers.ModelSerializer):
    """Serializer for the Color model to handle data validation and transformation."""
    class Meta:
        """Meta class that defines model and fields for the Color serializer."""
        model = Color
        fields = ["name"]


class SizeSerializer(serializers.ModelSerializer):
    """Serializer for the Size model to handle data validation and transformation."""
    class Meta:
        """Meta class that defines model and fields for the Size serializer."""
        model = Size
        fields = ["name"]


class BrandSerializer(serializers.ModelSerializer):
    """Serializer for the Brand model to handle data validation and transformation."""
    class Meta:
        """Meta class that defines model and fields for the Brand serializer."""
        model = Brand
        fields = ["name"]


class MaterialSerializer(serializers.ModelSerializer):
    """Serializer for the Material model to handle data validation and transformation."""
    class Meta:
        """Meta class that defines model and fields for the Material serializer."""
        model = Material
        fields = ["name"]


class ProductImageSerializer(serializers.ModelSerializer):
    """Serializer for the ProductImage model to handle data validation and transformation."""
    class Meta:
        """Meta class that defines model and fields for the ProductImage serializer."""
        model = ProductImages
        fields = ["image", "thumbnail"]


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for the Product model to handle data validation and transformation."""

    material = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Material.objects.all()   # pylint: disable=no-member
    )
    brand = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Brand.objects.all()    # pylint: disable=no-member
    )
    size = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Size.objects.all()  # pylint: disable=no-member
    )
    color = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Color.objects.all()  # pylint: disable=no-member
    )
    subcategory = serializers.PrimaryKeyRelatedField(
        many=True, queryset=SubCategory.objects.all()  # pylint: disable=no-member
    )

    product_images = ProductImageSerializer(
        many=True, required=False, read_only=True)

    subcategory = serializers.SlugRelatedField(
        queryset=SubCategory.objects.all(),  # pylint: disable=no-member
        slug_field='slug',  # Look up by the slug of Category
        required=True
    )

    class Meta:
        """Meta class that defines model and fields for the Product serializer."""
        model = Product
        fields = ["title", "description", "price",
                  "slug", "subcategory", "color", "brand", "size", "material", "stock", "active", "manufacturer", "featured", "product_images"]
        read_only_fields = ['slug']
