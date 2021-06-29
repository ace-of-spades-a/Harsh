from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, ProductCategory
# Create your views here.

def index(request):
    # return HttpResponse("Welcome to padmavati Export")
    Product_categs = ProductCategory.objects.all()
    products = Product.objects.all()
    
    return render(request, 'index/index.html', {'products' : products, 'product_catg' : Product_categs})

# def ajexCall(self, request):
#     import pdb;pdb.set_trace
#     text = request.GET.get('categ')

def validate_username(request):
    if request:
        categ = request.GET.get('categ')
        Product_categs = ProductCategory.objects.all()
        product_categ = ProductCategory.objects.get(prodcut_categ = categ)
        products = Product.objects.filter(product_categ_id = product_categ.id)
    return render(request, 'index/index.html', {'products' : products, 'product_catg' : Product_categs})
    # return render(products)

def test(request):
    import pdb;pdb.set_trace()