from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('category_list/', views.category_list, name='category_list'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('update_category/<int:category_id>/', views.update_category, name='update_category'),
    path('product_list/', views.product_list, name='product_list'),
    path('delete_product/<int:code>/', views.delete_product, name='delete_product'),
    path('update_products/<int:pk>/', views.update_products, name='update_products'),
    path('export_pdf/', views.export_pdf, name='export_pdf'),
    path('export_excel/', views.export_excel, name='export_excel'),
    path('import_excel/', views.import_excel, name='import_excel'),
    path('export_import/', views.export_import, name='export_import'),
    #path('add_product/', views.add_product, name='add_product'),
    #path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    #path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    #path('index/', views.index, name='index'),
]