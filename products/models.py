""" products/models.py """
from autoslug import AutoSlugField

from django.db import models
from django.core.validators import MinValueValidator, FileExtensionValidator

from core.models import TimeStampedModel


class ParentCategory(TimeStampedModel):
    """ParentCategory model"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='parent_category_img/%Y/%m/%d/', blank=True, null=True, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'webp'])])

    slug = AutoSlugField(populate_from='name',
                         db_index=True,
                         unique=True, always_update=False)

    class Meta:
        """Meta class for Category model"""
        verbose_name = "Parent Category"
        verbose_name_plural = "Parent Categories"

    def __str__(self):
        return f"{self.name}"


class Category(TimeStampedModel):
    """Category model"""
    name = models.CharField(max_length=100, unique=True)
    parent_category = models.ForeignKey(
        ParentCategory, on_delete=models.CASCADE, related_name='categories')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='category_img/%Y/%m/%d/', blank=True, null=True, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'webp'])])

    slug = AutoSlugField(populate_from='name',
                         db_index=True,
                         unique=True, always_update=False)

    class Meta:
        """Meta class for Category model"""
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        unique_together = ('name', 'parent_category')

    def __str__(self):
        return f"{self.name}"


class SubCategory(TimeStampedModel):
    """SubCategory model"""
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='subcategories')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='subcategory_img/%Y/%m/%d/', blank=True, null=True, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'webp'])])
    slug = AutoSlugField(populate_from='name',
                         db_index=True,
                         unique=True, always_update=False)

    class Meta:
        """Meta class for Category model"""
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"
        unique_together = ('name', 'category')

    def __str__(self):
        return f"{self.name}"


class Color(TimeStampedModel):
    """Color model"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Size(TimeStampedModel):
    """Size model"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Brand(TimeStampedModel):
    """Brand model"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Material(TimeStampedModel):
    """Material model"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Product(TimeStampedModel):
    """Products model"""

    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[
                                MinValueValidator(0.0)])
    slug = AutoSlugField(populate_from='name',
                         db_index=True,
                         unique=True, always_update=False)

    # product options
    subcategory = models.ManyToManyField(
        SubCategory, blank=True, related_name="products")
    color = models.ManyToManyField(Color, blank=True, related_name="products")
    size = models.ManyToManyField(Size, blank=True, related_name="products")
    brand = models.ManyToManyField(
        Brand, blank=True, related_name="products")
    material = models.ManyToManyField(
        Material, blank=True, related_name="products")

    stock = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    active = models.BooleanField(default=False)
    manufacturer = models.CharField(max_length=250)
    featured = models.BooleanField(default=False)
    thumbnail = models.ImageField(
        upload_to='thumbnails/%Y/%m/%d/')

    def __str__(self):
        return f"{self.title} (${self.price})"


class ProductImages(models.Model):
    """Product Images"""
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(
        upload_to='products/%Y/%m/%d/')

    def __str__(self):
        return f"{self.product.title} - Image"  # pylint: disable=no-member
