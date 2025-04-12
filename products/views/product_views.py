# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# from django.shortcuts import get_object_or_404

# from products.models import ParentCategory, Category, SubCategory
# from products.serializers import ParentCategorySerializer, CategorySerializer, SubCategorySerializer


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from products.models import Product
from products.serializers import ProductSerializer


@api_view(['GET', 'POST'])
def product_crud(request, product_slug=None):
    """Handles CRUD operations for Product."""
    if request.method == 'GET':
        if product_slug is not None:
            product = get_object_or_404(Product, slug=product_slug)
            serializer = ProductSerializer(
                product, context={'request': request})
            return Response(serializer.data)
        else:
            products = Product.objects.all()  # pylint: disable=no-member
            serializer = ProductSerializer(
                products, many=True, context={'request': request})
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

