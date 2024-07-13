from django.shortcuts import render, redirect
from phones.models import Phone 

def index(request):
    return redirect('catalog')

def show_catalog(request):
    sort = request.GET.get('sort', 'id')
    if sort == 'min_price':
        sort='price'
    elif sort == 'max_price':
        sort='-price'
    phones = Phone.objects.all().order_by(sort)
    context = {'phones':phones}
    template = 'catalog.html'
    return render(request, template, context)

def show_product(request, slug):
    phones = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phones}
    return render(request, template, context)