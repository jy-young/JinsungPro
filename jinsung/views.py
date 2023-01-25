from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render,redirect
from .models import Post


def index(request):
    return render(request, 'jinsung/index.html')

def products(request):
    return render(request, 'jinsung/product.html')

def products_update(request):
    if request.method == "POST":
        print(request.POST.get('tag'))
        data = {
            'title':request.POST.get('title'),
            'content': request.POST.get('content'),
            'tag':request.POST.get('tag')
        }
        Post.objects.create(**data)

        return redirect(f'/products/')
    context = {
        'tags': Post.all_tags
    }
    return render(request, 'jinsung/product_update.html',context)
