from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from .forms import BookForm
from django.contrib import messages
import sweetify

# Create your views here.
def books_list(request):
    books = models.Book.objects.all()
    context = {'books': books} #, 'name':'Juan'}

    #messages.error(request, 'testing')    
    #sweetify.success(request, 'You successfully changed your password')
    #sweetify.toast(request, 'Cheers to new toast')
    
    return render(request, 'books_list.html', context)

def book_detail(request, pk):
    book = models.Book.objects.get(pk=pk)
    context = {'book': book}
    return render(request, 'books_detail.html', context)

def new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            #print("guardado exitosamente")
            #messages.success(request, 'Libro guardado correctamente')
            sweetify.toast(request, 'Libro guardado correctamente')

            return redirect('/books')
    else:
        form = BookForm()
        #print("no se pudo guardar")
        return render(request, 'new_book.html', {'form':form})

def edit_book(request, pk):
    book = models.Book.objects.get(pk = pk)
    form = BookForm(request.POST, instance=book)
    if form.is_valid():
        form.save()
        #print("editado exitosamente")
        messages.success(request, 'Libro editado correctamente')
        return redirect('/books')
    #else: 
        #print("no se pudo editar")        
    return render(request, 'edit_book.html', {'book':book, 'states': models.Book.STATUS, 'types':models.Book.TIPOS_BOOK})
    
    
def delete_book(request,pk):
    book = models.Book.objects.get(pk=pk)
    book.delete()
    messages.warning(request, 'Libro eliminado correctamente')
    return redirect('/books')