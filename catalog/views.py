from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from django.views.generic import TemplateView, ListView, DetailView



class HomeView(TemplateView):
    template_name = "catalog/home.html"


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/products_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/products_detail.html'
    context_object_name = 'product'
