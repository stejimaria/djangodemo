from django.shortcuts import render
from shop.models import Product
from django.db.models import Q


# Create your views here.

def search_products(request):
    query=""
    p=None
    if(request.method=="POST"):
        query=request.POST['q']
        print(query)
        if query:
            p=Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request,'search.html',{'product':p,'q':query})