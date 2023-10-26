from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from .models import Product
from .forms import ProductUpdateForm
from .models import Category
from django.http import JsonResponse
# libraries for Import Export 
from import_export.formats import base_formats 
from django.http import HttpResponse
from import_export.resources import modelresource_factory
from .resources import ProductResources
from tablib import Dataset
from reportlab.pdfgen import canvas
from import_export import resources
from import_export.resources import ModelResource



#===============================================================code for category========================================

#====== list and add category======================
def category_list(request):
    queryset = Category.objects.all()
    if request.method == "POST":       # Add Categories
        formbb = CategoryForm(request.POST or None)
        if formbb.is_valid():
            formbb.save()
        return redirect('category_list')
    else:
        formbb = CategoryForm()
    context = {
        "queryset":queryset,
        "formbb": formbb,
    }
    return render(request, "category_list.html", context)



#============= delete category===================
def delete_categorys(request, pk):
    queryset = get_object_or_404(Category, pk=pk) # used to get the product
    if request.method == 'POST':
        queryset.delete()
        return redirect('category_list')
    return redirect('category_list')




#===========================================================the for Products page==========================================



#=========== list and Add product ===========================
def product_list(request):
    queryset = Product.objects.all()
    if request.method == 'POST':    # Add Products
        formcc = ProductForm(request.POST)
        if formcc.is_valid():
            formcc.save()
            return redirect('product_list')
    else:
        formcc = ProductForm()

    queryset = Product.objects.all().order_by('product_name')
    context ={
        "queryset":queryset,
        "formcc":formcc,
    }
    return render(request, "product_list.html", context)




#====================================== Add product to main Store=======================================
def receive_products(request, code):
    queryset = Product.objects.get(code=code)
    formjj= ProductAmendForm(request.POST or None, instance=queryset)
    if formjj.is_valid():
        instance= formjj.save(commit=False)
        instance.shop_send_quantity = 0   # set the value of the "issue to shop" =0
        instance.factory_quantity += instance.receive_main_quantity   # add the received quantity from factory to the quantity in the store
        instance.first_add_main_quantity = instance.receive_main_quantity+instance.first_add_main_quantity # recording the products that are stored in main store from the first record of received itme until now
        instance.save()
        return redirect ("product_list")
    context = {
        "instance":queryset,
        "formjj":formjj,
    }
    return render(request, 'receive_products.html',context)





#===================== issue products from main store to shop store================================

def issue_products(request, code):
    queryset = Product.objects.get(code=code)
    formuu= ProductIssueForm(request.POST or None, instance=queryset)
    if formuu.is_valid():
        instance= formuu.save(commit=False)
        instance.receive_main_quantity=0
        instance.factory_quantity -= instance.shop_send_quantity
        instance.shop_receive_quantity = instance.shop_receive_quantity+ instance.shop_send_quantity
        instance.shop_remain_quantity +=instance.shop_send_quantity
        instance.save()
        return redirect ("product_list")
    context = {
        "instance":queryset,
        "formuu":formuu,
    }
    return render(request, 'issue_products.html',context)



#====================== delete products from the list====================

def delete_product(request, code):
    queryset = get_object_or_404(Product, code=code)
    if request.method == 'POST':
        queryset.delete()
        return redirect('product_list')
    return redirect('product_list')




#======================= Update the Products =================================
def update_products(request, code):
          queryset= Product.objects.get(code=code)
          formvv= ProductUpdateForm(instance = queryset)
          if request.method == 'POST':
                    formvv = ProductUpdateForm(request.POST,instance=queryset)
                    if formvv.is_valid():
                              formvv.save()
                              return redirect('product_list')
          context= {
              'formvv' : formvv
          }
          return render(request, 'update_products.html', context)




#=================================================================for the shop store =============================================
def shop_sell(request):
    return render(request, 'shop_sell.html')

def product_shop_list(request):
    queryset = Product.objects.all()
    queryset = Product.objects.all().order_by('product_name')
    context ={
        "queryset":queryset,
    }
    return render(request, "product_shop_list.html", context)
 
 
 #==================== code for the import and Export=========================================

class ProductResource(ModelResource):
    class Meta:
        model = Product


def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="products.pdf"'
    p = canvas.Canvas(response)

    product = Product.objects.all()
    for item in product:
        p.drawString(100, 700, f'Name: {item.product_name}')
        p.drawString(100, 680, f'Description: {item.description}')
        p.showPage()

    p.save()
    return response

def export_excel(request):
    product = ProductResource().export()
    response = HttpResponse(product.xls, content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="product.xls"'
    return response

def import_excel(request):
    if request.method == 'POST':
        dataset = Dataset()
        new_data = request.FILES['myfile']

        if not new_data.name.endswith('xls'):
            messages.info(request, 'Wrong format')
            return render(request, 'import_data.html')

        imported_data = dataset.load(new_data.read(), 'xls')
        result = ProductResource().import_data(dataset, dry_run=True)  # Check if the data is valid
        if not result.has_errors():
            ProductResource().import_data(dataset, dry_run=False)  # Import the actual data
            messages.success(request, 'Data imported successfully')

    return render(request, 'import_data.html')

def export_import(request):
    return render(request, 'product_list.html')