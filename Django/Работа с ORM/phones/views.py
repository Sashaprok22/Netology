from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')

def show_catalog(request):
    sort_type = request.GET.get("sort")
    template = 'catalog.html'

    if sort_type == " name":
        phones = Phone.objects.order_by("name")
    elif sort_type == "max_price":
        phones = Phone.objects.order_by("price").reverse()
    elif sort_type == "min_price":
        phones = Phone.objects.order_by("price")
    else:
        phones = Phone.objects.all()

    context = {
        "phones": phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        "phone": Phone.objects.filter(slug=slug)[0]
    }
    return render(request, template, context)
