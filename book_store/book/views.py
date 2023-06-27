from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
from django.views.generic import TemplateView, ListView,DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

#function base view
def home(request):
    return render(request,'home.html')

# class base view
class MyTempalteView(TemplateView):
    template_name='home.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context={'name': 'rahim','age':21}
        return context
my_view=MyTempalteView.as_view()

# def store_book(request):
#     if request.method=='POST':
#         book=BookStoreForm(request.POST)
#         if book.is_valid():
#             book.save()
#             print(book.cleaned_data)
#             return redirect('show_books')    
#     else:
#         book=BookStoreForm()    
#     return render (request,'store_book.html',{'form':book})

# class BookFormView(FormView):
#     template_name='store_book.html'
#     form_class=BookStoreForm
#     # success_url=reverse_lazy('show_books')
#     def form_valid(self,form):
#         form.save()
#         return redirect('show_books')


class BookFormView(CreateView):
    model=BookStoreModel
    template_name='store_book.html'
    form_class=BookStoreForm
    success_url=reverse_lazy('show_books')
  



# def show_books(request):
#     book=BookStoreModel.objects.all()
#     return render (request,'show_book.html',{'data':book})

#class base view
class book_list_view(ListView):
    model=BookStoreModel
    template_name='show_book.html'
    context_object_name='data'
    # def get_queryset(self):
    #     return BookStoreModel.objects.filter()
    # def get_context_data(self,**kwargs):
    #     context=super().get_context_data(**kwargs)
    #     context={'Rahim':BookStoreModel.objects.filter()}
    #     return context    
    # ordering=['id']
    
    
class BookDetailView(DetailView):
    model=BookStoreModel
    template_name='book_details.html'
    context_object_name='item'
    pk_url_kwarg='id'
    
    

def edit_book(request,id):
    book=BookStoreModel.objects.get(pk=id)
    form=BookStoreForm(instance=book)
    if request.method=="POST":
        info=BookStoreForm(request.POST, instance=book)
        if info.is_valid():
            info.save()
            return redirect('show_books')
    return render (request,'store_book.html',{'form':form})

class BookUpdateView(UpdateView):
    model=BookStoreModel
    template_name='store_book.html'
    form_class=BookStoreForm
    success_url=reverse_lazy('show_books')


class DeleteBookView(DeleteView):
    model=BookStoreModel
    template_name='delete_confirmation.html'
    success_url=reverse_lazy('show_books')

# def delete_book(request,id):
#     book=book=BookStoreModel.objects.get(pk=id).delete()
#     return redirect ('show_books')