"""View functions for products models."""

from typing import Any

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import ParentCategory
from products.serializers import ParentCategorySerializer


@api_view(['GET', 'POST'])
def parent_category_cr(request: Any):
    """View to create a new parent category."""
    if request.method == 'GET':
        parent_categories = ParentCategory.objects.all()  # pylint: disable=no-member
        serializer = ParentCategorySerializer(
            parent_categories, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ParentCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
