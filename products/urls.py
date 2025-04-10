"""URL configuration for the project."""

from django.urls import path

from products.views import (
    parent_category_crud,
)

urlpatterns = [
    path("parent-category/", parent_category_crud,
         name="parent_category_create"),
]
