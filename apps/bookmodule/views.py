from django.shortcuts import render
from django.http import HttpResponse


def index(request):
 return render(request, "bookmodule/index.html")

def index2(request, val1=0):
   return HttpResponse("value1 = " + str(val1))

def list_books(request):
 return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}

    # Find the target book
    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    elif book2['id'] == bookId:
        targetBook = book2

    context = {'book': targetBook}  # 'book' is the variable name accessible by the template

    return render(request, 'bookmodule/one_book.html', context)

def aboutus(request):
 return render(request, 'bookmodule/aboutus.html')

def links_page(request):
  return render(request, 'bookmodule/links.html') 

def formatting_page(request):
  return render(request, 'bookmodule/formatting.html')  

def listing_page(request):
  return render(request, 'bookmodule/listing.html') 

def tables_page(request):
  return render(request, 'bookmodule/tables.html') 