from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("products/", views.products, name='products'),
    path("products_update/", views.products_update, name='products_update'),
    path("products_detail/<int:pk>", views.products_detail, name='products_detail'),
    path("pro_tag/", views.pro_tag, name='pro_tag'),
]