from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render,redirect
from .models import Post
from django_summernote.widgets import SummernoteWidget


def index(request):
    return render(request, 'jinsung/index.html')

def products(request):
    products = Post.objects.all()

    if request.method == "POST": #검색기능
        search = request.POST.get('search')
        products = Post.objects.filter(title__contains = search)

    context = {
        'products':products,
        'tags': Post.all_tags,
    }
    return render(request, 'jinsung/product.html',context)

def pro_tag(request):
    tag = request.GET.get('tag')
    products = Post.objects.filter(tag = tag)
    context = {
        'products':products,
        'tags': Post.all_tags,
    }
    return render(request, 'jinsung/product.html',context)

def products_update(request):
    if request.method == "POST":
        data = {
            'title':request.POST.get('title'),
            'content': request.POST.get('content'),
            'tag':request.POST.get('tag')
        }
        Post.objects.create(**data)

        return redirect(f'/products/')
    context = {
        'tags': Post.all_tags,
    }
    return render(request, 'jinsung/product_update.html',context)

def products_detail(request, pk):
    point = Post.objects.get(pk = pk)
    context = {
        'point' : point
    }
    return render(request, 'jinsung/product_detail.html', context)
