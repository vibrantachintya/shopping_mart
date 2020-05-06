from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Product, Category, Company
# Create your views here.

def crud(request):

    products = Product.objects.all()
    categories = Category.objects.all()
    companies = Company.objects.all()
    
    params = {'products': products, 'categories' : categories, 'companies' : companies}

    return render(request, 'shop/index.html', params)

def showcategory(request, cat):

    categories = Category.objects.all()
    companies = Company.objects.all()

    cats = Category.objects.get(name=cat)

    products = Product.objects.filter(category=cats).values()

    params = {'products' : products, 'category' : cat, 'categories' : categories, 'companies' : companies}

    return render(request, 'shop/category.html', params)


def showcompany(request, comp):

    categories = Category.objects.all()
    companies = Company.objects.all()

    comps = Company.objects.get(name=comp)

    products = Product.objects.filter(company=comps).values()

    params = {'products' : products, 'category' : comp, 'categories' : categories, 'companies' : companies}

    return render(request, 'shop/category.html', params)

def showproduct(request, product_id):

    product = Product.objects.get(id=product_id)
    related = Product.objects.exclude(id=product_id).values

    params = {'product' : product, 'related' : related}

    return render(request, 'shop/product.html', params)