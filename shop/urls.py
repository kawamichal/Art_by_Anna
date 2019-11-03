from django.urls import path

from shop import views

app_name = 'shop'
urlpatterns = [
    path('', views.CategoryList.as_view(), name='categories'),
    path('<slug:category_slug>/', views.ProductByCategoryView.as_view(), name='products_by_category'),
    path('detail/<slug:slug>/', views.ProductDetail.as_view(), name='product_detail')
]
