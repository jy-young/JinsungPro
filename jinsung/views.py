from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render,redirect
from .models import Post
from django_summernote.widgets import SummernoteWidget
from django.core.paginator import Paginator


def index(request):
    pd1 = Post.objects.get_queryset().order_by('-id')[:4]
    pd2 = Post.objects.get_queryset().order_by('-id')[5:9]
    context = {
        'pd1':pd1,
        'pd2':pd2
    }
    return render(request, 'jinsung/index.html',context)

def products(request):
    page = request.GET.get('page','1')
    products = Post.objects.get_queryset().order_by('id')

    if request.method == "POST": #검색기능
        search = request.POST.get('search')
        products = Post.objects.filter(title__contains = search)
    
    # 페이징
    paginator = Paginator(products, 8)
    page_obj = paginator.get_page(page)

    context = {
        'products':page_obj,
        'tags': Post.all_tags,
    }
    return render(request, 'jinsung/product.html',context)

def pro_tag(request):
    tag = request.GET.get('tag')
    if tag == None:
        tag = request.session['tag']
    else:
        request.session['tag'] = tag
    
    products = Post.objects.filter(tag = tag)

    # 페이징
    page = request.GET.get('page','1')
    paginator = Paginator(products, 8)
    page_obj = paginator.get_page(page)

    context = {
        'products':page_obj,
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
        'point' : point,
        'tags': Post.all_tags,
    }
    return render(request, 'jinsung/product_detail.html', context)

def intro(request):
    return render(request,'jinsung/intro.html')