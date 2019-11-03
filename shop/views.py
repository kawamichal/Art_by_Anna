from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from shop.models import Category, Product


class CategoryList(ListView):
    queryset = Category.objects.all()
    model = Category
    template_name = 'shop/categories.html'


class ProductByCategoryView(ListView):
    queryset = Product.objects.filter(available=True)
    model = Product
    template_name = 'shop/products.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        return Product.objects.filter(category=self.category)

class ProductDetail(DetailView):
    queryset = Product.objects.filter(available=True)
    model = Product
    template_name = 'shop/product_detail.html'

