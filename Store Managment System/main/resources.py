from import_export import resources
from .models import Product

class ProductResources(resources.ModelResource):
    class Meta:
        model = Product