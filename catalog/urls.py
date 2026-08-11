from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.product_list, name="product-list"),
    path("products/export/", views.product_export, name="product-export"),
    path("quote/", views.quote, name="quote"),
]
