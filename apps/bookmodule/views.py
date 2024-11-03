from django.shortcuts import render
from django.http import HttpResponse


def index(request):
 return render(request, "bookmodule/index.html")

def index2(request, val1=0):
   return HttpResponse("value1 = " + str(val1))

def list_books(request):
 return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
  return render(request, 'bookmodule/one_book.html')

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

def __getBooksList():
  
  book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
  book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
  book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
  
  return [book1, book2, book3]

def search_books(request):
    if request.method == "POST":
        return handle_search(request)
    return render(request, 'bookmodule/search.html')

def handle_search(request):
    string = request.POST.get('keyword', '').lower()
    isTitle = request.POST.get('option1')
    isAuthor = request.POST.get('option2')
    
    # Retrieve the list of books
    books = __getBooksList()
    newBooks = []
    
    for item in books:
        contained = False
        if isTitle and string in item['title'].lower():
            contained = True
        if not contained and isAuthor and string in item['author'].lower():
            contained = True
            
        if contained:
            newBooks.append(item)

    return render(request, 'bookmodule/bookList.html', {'books': newBooks})