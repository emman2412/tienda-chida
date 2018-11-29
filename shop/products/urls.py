from django.conf.urls import url
from django.urls import path
from . import views
from .views import ProductCreate, ProductUpdate, ProductDelete
app_name = 'products'

products_patterns = ([
    path('', views.product_list, name='product_list'),
    path('results/', views.search, name='search'),
    path('order_name/', views.order_name, name='order_name'),
    path('order_price/', views.order_price, name='order_price'),
    path('category/<category_slug>/', views.category, name='product_list_by_category'),
    path('trademark/<trademark_slug>/', views.trademark, name='product_list_by_trademark'),
    path('<id>/<slug>/', views.product_detail, name='product_detail'),
    path('create/', ProductCreate.as_view(), name='create'),
    path('update/<id>/<slug>/', ProductUpdate.as_view(), name='update'),
    path('delete/<id>/<slug>/', ProductDelete.as_view(), name='delete'),
], 'products')
