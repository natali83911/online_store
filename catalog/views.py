from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product


class OwnerOrModeratorMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        user = self.request.user
        if user.groups.filter(
            name=settings.MODERATOR_GROUP_NAME
        ).exists() and user.has_perm("catalog.can_unpublish_product"):
            return True

        return obj.owner == user

    def handle_no_permission(self):
        raise PermissionDenied


class HomeView(TemplateView):
    template_name = "catalog/home.html"


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductsListView(ListView):
    model = Product
    template_name = "catalog/products_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/products_detail.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, OwnerOrModeratorMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:products_list")

    def get_form_class(self):
        user = self.request.user
        obj = self.get_object()
        if obj.owner == user:
            return ProductForm
        if user.groups.filter(name=settings.MODERATOR_GROUP_NAME).exists():
            return ProductModeratorForm
        return PermissionDenied

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name=settings.MODERATOR_GROUP_NAME).exists():
            return Product.objects.all()
        return Product.objects.filter(owner=user)


class ProductDeleteView(LoginRequiredMixin, OwnerOrModeratorMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:products_list")

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name=settings.MODERATOR_GROUP_NAME).exists():
            return Product.objects.all()
        return Product.objects.filter(owner=user)
