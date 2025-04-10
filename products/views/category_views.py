"""View functions for products models."""


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from products.models import ParentCategory, Category
from products.serializers import ParentCategorySerializer, CategorySerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def parent_category_crud(request):
    """Handles CRUD operations for ParentCategory."""

    if request.method == 'GET':
        parent_categories = ParentCategory.objects.all()  # pylint: disable=no-member
        serializer = ParentCategorySerializer(
            parent_categories, many=True, context={'request': request}
        )
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ParentCategorySerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        parent_category_id = request.data.get('id')
        if not parent_category_id:
            return Response({'error': 'Parent category ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        parent_category = get_object_or_404(
            ParentCategory, id=parent_category_id)
        serializer = ParentCategorySerializer(
            parent_category, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        parent_category_id = request.data.get('id')
        if not parent_category_id:
            return Response({'error': 'Parent category ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        parent_category = get_object_or_404(
            ParentCategory, id=parent_category_id)
        parent_category.delete()
        return Response({'detail': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def category_crud(request):
#     """Handles CRUD operations for Category."""

#     if request.method == 'GET':
#         parent_categories = Category.objects.all()  # pylint: disable=no-member
#         serializer = CategorySerializer(
#             parent_categories, many=True, context={'request': request}
#         )
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = CategorySerializer(
#             data=request.data, context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'PUT':
#         parent_category_id = request.data.get('id')
#         if not parent_category_id:
#             return Response({'error': 'Category ID is required'}, status=status.HTTP_400_BAD_REQUEST)

#         parent_category = get_object_or_404(
#             Category, id=parent_category_id)
#         serializer = CategorySerializer(
#             parent_category, data=request.data, context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         parent_category_id = request.data.get('id')
#         if not parent_category_id:
#             return Response({'error': 'Category ID is required'}, status=status.HTTP_400_BAD_REQUEST)

#         parent_category = get_object_or_404(
#             Category, id=parent_category_id)
#         parent_category.delete()
#         return Response({'detail': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
