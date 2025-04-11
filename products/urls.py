"""URL configuration for the project."""

from django.urls import path

from products.views import (
    parent_category_crud,
    category_crud,
    sub_category_crud
)


urlpatterns = [
    path("parent-category/", parent_category_crud,
         name="parent_category_create"),
    path("parent-category/<str:parent_category_slug>/", parent_category_crud,
         name="parent_category_update"),

    path("category/", category_crud, name="category_create"),
    path("category/<str:category_slug>/",
         category_crud, name="category_update"),

    path("sub-category/", sub_category_crud, name="sub_category_create"),
    path("sub-category/<str:sub_category_slug>/",
         sub_category_crud, name="sub_category_update"),
]
