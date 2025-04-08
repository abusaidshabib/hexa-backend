from rest_framework import serializers

from .models import Product, ProductImages


class ProductSerializer(serializers.models):
    class Meta:
        models = Product
        fields = ["title", "description", "price", "stock"]
