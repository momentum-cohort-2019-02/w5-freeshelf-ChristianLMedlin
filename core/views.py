from django.shortcuts import render
from .models import Author, Book, Programming_Languages
# Create your views here.

def home(request):
    return render(request, 'core/base.html')
