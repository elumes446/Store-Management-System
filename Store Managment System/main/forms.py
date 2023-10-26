from django import forms
from django.forms.models import inlineformset_factory
from main.models import *
from django.forms.models import inlineformset_factory
from django import forms
from .models import Category
from django import forms
from .models import Category
from django.core.validators import MinValueValidator
from .models import Product
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'description']
    def clean_category_name(self):
        category_name = self.cleaned_data.get('category_name')
        # Check if a category with the same name (case-insensitive) already exists
        existing_category = Category.objects.filter(category_name__iexact=category_name).first()
        if existing_category:
            raise forms.ValidationError("A category with this name already exists.")
        return category_name


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'description', 'price', 'status']

    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        # Check if a product with the same name (case-insensitive) already exists
        existing_product = Product.objects.filter(product_name__iexact=product_name).exclude(pk=self.instance.pk).first()
        if existing_product:
            raise forms.ValidationError("A product with this name already exists.")
        return product_name

class ProductAmendForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['receive_main_quantity']

    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        # Check if a product with the same name (case-insensitive) already exists
        existing_product = Product.objects.filter(product_name__iexact=product_name).exclude(pk=self.instance.pk).first()
        if existing_product:
            raise forms.ValidationError("A product with this name already exists.")
        return product_name

class ProductIssueForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['shop_send_quantity']

    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        # Check if a product with the same name (case-insensitive) already exists
        existing_product = Product.objects.filter(product_name__iexact=product_name).exclude(pk=self.instance.pk).first()
        if existing_product:
            raise forms.ValidationError("A product with this name already exists.")
        return product_name

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'description', 'price', 'status']
    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        # Check if a product with the same name (case-insensitive) already exists
        existing_product = Product.objects.filter(product_name__iexact=product_name).exclude(pk=self.instance.pk).first()
        if existing_product:
            raise forms.ValidationError("A product with this name already exists.")
        return product_name