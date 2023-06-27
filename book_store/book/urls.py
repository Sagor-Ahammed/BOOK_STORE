from django.contrib import admin
from django.urls import path,include
# from book.views import home,store_book,show_books,edit_book,delete_book
from . import views

urlpatterns = [
    path('',views.home , name="homepage"),
    path('<int:roll>/',views.MyTempalteView.as_view(),name='my_view'),
    # path('store_new_book/',views.store_book,name="storebook"),
    path('store_new_book/',views.BookFormView.as_view(),name="storebook"),
    # path('show_book/',views.show_books,name="show_books"),
    path('book_details/<int:id>',views.BookDetailView.as_view(),name="book_details"),
    path('show_book/',views.book_list_view.as_view(),name="show_books"),
    # path('edit_book/<int:id>',views.edit_book,name="edit_book"),
    path('edit_book/<int:pk>',views.BookUpdateView.as_view(),name="edit_book"),
    # path('delete_book/<int:id>',views.delete_book,name="delete_book"),
    path('delete_book/<int:pk>',views.DeleteBookView.as_view(),name="delete_book"),
]
