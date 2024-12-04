from django.shortcuts import render
from shop.models import Books
from django.core.cache import cache


   def home(request):
    books=Books.objects.all()
    return render(request,'home.html',{'books':books})

def cart(request):
    return render(request, 'cart.html')

def product_list(request):
    product_list = cache.get('product_list')

    if product_list is None:
        # If not in cache, fetch the data from the database
        product_list = list(Books.objects.all())  # Convert QuerySet to list

        # Store the product list in the cache for 15 minutes (900 seconds)
        cache.set('product_list', product_list, 900)

    return render(request, 'home.html', {'products': product_list})
