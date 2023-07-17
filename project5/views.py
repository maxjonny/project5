from django.shortcuts import render
from os import path
# Create your views here.


def home_view(request):
    return render(request, "project5/index.html", context={})

def product_view(request):
    return render(request, "project5/products.html", context={})


