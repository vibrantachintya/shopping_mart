from django.http import HttpResponse
from django.shortcuts import render

from .models import Product, Category, Company
# Create your views here.

def crud(request):

    products = Product.objects.all()
    categories = Category.objects.all()
    companies = Company.objects.all()
    params = {'products': products, 'categories' : categories, 'companies' : companies}


    return render(request, 'shop/index.html', params)