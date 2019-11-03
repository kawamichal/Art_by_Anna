from django.contrib import admin

from shop.models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created']
    list_editable = ['price', 'available']  # editable columns from the level of list display
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['category']
