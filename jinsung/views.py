from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from .forms import PostForm
from .models import Post


def index(request):
    return render(request, 'jinsung/index.html')

def products(request):
    return render(request, 'jinsung/product.html')

def products_update(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            return redirect('/products/')
    else:
        form = PostForm()
    return render(request, 'jinsung/product_update.html')
