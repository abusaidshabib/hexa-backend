"""View functions for products models."""


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from products.models import ParentCategory, Category, SubCategory
from products.serializers import ParentCategorySerializer, CategorySerializer, SubCategorySerializer

#    if request.method == 'GET':
#        print(category_slug)
#        if category_slug is not None:
#             category = get_object_or_404(Category, slug=category_slug)

#         else:
#             categories = Category.objects.all()  # pylint: disable=no-member
#             serializer = CategorySerializer(
#                 categories, many=True, context={'request': request})
#             return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def parent_category_crud(request, parent_category_slug: str = None):
    """Handles CRUD operations for ParentCategory."""

    if request.method == 'GET':
        if parent_category_slug is not None:
            parent_category = get_object_or_404(
                ParentCategory, slug=parent_category_slug)
            serializer = ParentCategorySerializer(
                parent_category, context={'request': request})
            return Response(serializer.data)
        else:
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
        if not parent_category_slug:
            return Response({'error': 'Parent category ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        parent_category = get_object_or_404(
            ParentCategory, slug=parent_category_slug)
        serializer = ParentCategorySerializer(
            parent_category, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if not parent_category_slug:
            return Response({'error': 'Parent category ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        parent_category = get_object_or_404(
            ParentCategory, slug=parent_category_slug)
        parent_category.delete()
        return Response({'detail': 'Deleted successfully'}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def category_crud(request, category_slug: str = None):
    """Handles CRUD operations for Category."""

    # Handle GET request - list all categories
    if request.method == 'GET':
        print(category_slug)
        if category_slug is not None:
            category = get_object_or_404(Category, slug=category_slug)
            serializer = CategorySerializer(
                category, context={'request': request})
            return Response(serializer.data)
        else:
            categories = Category.objects.all()  # pylint: disable=no-member
            serializer = CategorySerializer(
                categories, many=True, context={'request': request})
            return Response(serializer.data)

    # Handle POST request - create a new category
    elif request.method == 'POST':
        serializer = CategorySerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()  # Save the new category
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle PUT request - update an existing category
    elif request.method == 'PUT':
        if not category_slug:
            return Response({'error': 'Category ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        category = get_object_or_404(
            Category, slug=category_slug)  # Get the category object
        serializer = CategorySerializer(
            category, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()  # Save the updated category
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle DELETE request - delete a category
    elif request.method == 'DELETE':
        if not category_slug:
            return Response({'error': 'Category ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        category = get_object_or_404(
            Category, slug=category_slug)  # Get the category object
        category.delete()  # Delete the category
        return Response({'detail': 'Deleted successfully'}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def sub_category_crud(request, sub_category_slug: int = None):
    """Handles CRUD operations for Category."""

    # Handle GET request - list all categories
    if request.method == 'GET':
        if sub_category_slug is not None:
            sub_category = get_object_or_404(
                SubCategory, slug=sub_category_slug)
            serializer = SubCategorySerializer(
                sub_category, context={'request': request})
            return Response(serializer.data)
        else:
            sub_categories = SubCategory.objects.all()  # pylint: disable=no-member
            serializer = SubCategorySerializer(
                sub_categories, many=True, context={'request': request})
            return Response(serializer.data)

    # Handle POST request - create a new category
    elif request.method == 'POST':
        serializer = SubCategorySerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()  # Save the new category
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle PUT request - update an existing category
    elif request.method == 'PUT':
        if sub_category_slug is None:
            return Response({'error': 'Category slug is required'}, status=status.HTTP_400_BAD_REQUEST)

        sub_category = get_object_or_404(
            SubCategory, slug=sub_category_slug)  # Get the category object
        serializer = SubCategorySerializer(
            sub_category, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()  # Save the updated category
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle DELETE request - delete a category
    elif request.method == 'DELETE':
        if sub_category_slug is None:
            return Response({'error': 'Category slug is required'}, status=status.HTTP_400_BAD_REQUEST)

        category = get_object_or_404(
            SubCategory, slug=sub_category_slug)  # Get the category object
        category.delete()  # Delete the category
        return Response({'detail': 'Deleted successfully'}, status=status.HTTP_200_OK)
