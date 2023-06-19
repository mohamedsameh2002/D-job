from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *


# Create your views here.
def index (request):
    if request.method =='POST':
        add_book=BookForm(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()
            
        add_cat=CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()
            
    context={
        "books":Book.objects.all(),
        "cat":Category.objects.all(),
        "forms":BookForm(),
        "formcat":CategoryForm(),
        "allbooks":Book.objects.filter(active=True).count(),
        "bookssold":Book.objects.filter(starus="sold").count(),
        "booksrental":Book.objects.filter(starus="rental").count(),
        "booksavailble":Book.objects.filter(starus="availble").count(),
    }
    return render(request,'pages/index.html',context)
#=================================================================
def books (request):
    search=Book.objects.all()
    titel=None
    if 'search_name' in request.GET:
        titel=request.GET['search_name']
        if titel:
            search=search.filter(title__icontains=titel)




    context={
        "cat":Category.objects.all(),
        "books":search,
        "formcat":CategoryForm(),
    }
    return render(request,'pages/books.html',context)
#=================================================================

def update (request,id):
    book_id=Book.objects.get(id=id)
    if request.method == "POST":
        book_save=BookForm(request.POST,request.FILES,instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save=BookForm(instance=book_id)
    context={
        "form":book_save,
    }
    return render(request,'pages/update.html',context)

#=================================================================
def delete (request,id):
    book_delete=Book.objects.get(id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect ("/")

    return render(request,"pages/delete.html")



#=================================================================
