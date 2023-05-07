from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phone_objects = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort == 'max_price':
        phone_objects = phone_objects.order_by('-price')
    if sort == 'min_price':
        phone_objects = phone_objects.order_by('price')
    if sort == 'name':
        phone_objects = phone_objects.order_by('name')
    template = 'catalog.html'
    context = {'phones': phone_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    phone_objects = Phone.objects.all()
    for phone in phone_objects:
        if phone.slug == slug:
            context['phone'] = phone
    return render(request, template, context)
