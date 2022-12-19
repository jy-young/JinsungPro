from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render


def print_page(request):
    return render(request, 'base.html')
