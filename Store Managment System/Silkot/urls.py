"""
URL configuration for Silkot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category_list/', views.category_list, name='category_list'),
    path('delete_categorys/<int:pk>/', views.delete_categorys, name='delete_categorys'),
    path('product_list/', views.product_list, name='product_list'),
    path('delete_product/<int:code>/', views.delete_product, name='delete_product'),
    path('update_products/<int:code>/', views.update_products, name='update_products'),
    path('shop_sell/', views.shop_sell, name='shop_sell'),
    path('receive_products/<int:code>/', views.receive_products, name='receive_products'),
    path('issue_products/<int:code>/', views.issue_products, name='issue_products'),
    path('product_shop_list/', views.product_shop_list, name='product_shop_list'),
    path('export_pdf/', views.export_pdf, name='export_pdf'),
    path('export_excel/', views.export_excel, name='export_excel'),
    path('import_excel/', views.import_excel, name='import_excel'),
    path('export_import/', views.export_import, name='export_import'),
]
