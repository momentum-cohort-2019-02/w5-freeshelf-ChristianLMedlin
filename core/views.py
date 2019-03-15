from django.shortcuts import render
from .models import Author, Book, Programming_Languages
# Create your views here.

def home(request):
    
    book_list = {"books": Book.objects.all()}
    language_list = {"languages": Programming_Languages.objects.all()}
    
    return render(request, 'core/base.html', context={
        "books": Book.objects.all(),
        "languages": Programming_Languages.objects.all()
    })

    
