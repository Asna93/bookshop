from django.shortcuts import render
from shop.models import Books
from django.core.cache import cache

def book_list(request):
    book_list=cache.get('book_list')

    if book_list is None:
        book_list=list(Books.objects.all())

        cache.set('book_list',book_list,900)

    return render(request,'home.html',{'books':book_list})

   