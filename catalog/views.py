from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from catalog.models import Product
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:products_list')
