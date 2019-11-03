from django.urls import path

from shop import views

app_name = 'shop'
urlpatterns = [
    path('', views.CategoryList.as_view(), name='home'),
    path('categories/all/', views.ProductList.as_view(), name="all_products"),
    path('categories/<slug:slug>/', views.ProductByCategoryView.as_view(), name='products_by_category'),
    path('products/<slug:slug>/', views.ProductDetail.as_view(), name='product_detail')
]
