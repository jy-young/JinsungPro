from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'jinsung/index.html')

def products(request):
    return render(request, 'jinsung/product.html')

def products_update(request):
    return render(request, 'jinsung/product_update.html')
