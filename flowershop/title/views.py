from django.shortcuts import render,get_object_or_404
from .models import Product

def title(request):
    products = Product.objects.all()
    return render(request, "title/title.html", {"products": products , 'MEDIA_URL': '/media/'})

def products(request, product_id):
    product_list = get_object_or_404(Product, pk=product_id)
    return render(request, "title/product.html", {"product_list": product_list})

# Create your views here.
