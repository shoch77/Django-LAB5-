from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),

    path('html5/links', views.links_page, name='links'),
    path('html5/text/formatting', views.formatting_page, name='formatting'),
    path('html5/listing', views.listing_page, name='listing'),
    path('html5/tables', views.tables_page, name='tables'),

    path('search/', views.search_books, name='search_books'),
]