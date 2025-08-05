from django.urls import path
from catalog.views import products_list, products_detail, home, contacts

app_name = "catalog"

urlpatterns = [
    path("", home, name="home"),
    path("products/", products_list, name="products_list"),
    path("products/<int:pk>", products_detail, name="products_detail"),
    path("contacts/", contacts, name="contacts"),
]
