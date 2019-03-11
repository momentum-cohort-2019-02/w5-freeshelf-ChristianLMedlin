from django.db import models
from datetime import date

# Create your models here.

class Author(models.Model):
    """Contains identifying information about the Author to allow faciliation of searches based on previous works and author name."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    books_authored = models.ManyToManyField('Book', help_text="Names of all the books this author has contributed to", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




class Book(models.Model):
    """Contains information relating to the book."""
    title = models.CharField(max_length=50)
    book_author = models.ManyToManyField(Author, help_text="Enter the author/s of the book.")
    programming_language = models.CharField(max_length=30)
    description = models.TextField(max_length=1024, help_text="Enter a description of the book's topic")
    date_added = models.DateField(auto_now_add=True)
    #book_url = unknown info
    #book_slug = unknown info

    def __str__(self):
        return self.title
