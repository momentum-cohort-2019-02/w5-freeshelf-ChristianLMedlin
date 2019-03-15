from django.db import models
from datetime import datetime, date
from django.contrib.auth import get_user_model


User = get_user_model()


class Author(models.Model):
    """Contains identifying information about the Author to allow faciliation of searches based on previous works and author name."""
    name = models.CharField(max_length=150)
    books_authored = models.ManyToManyField('Book', help_text="Names of all the books this author has contributed to", blank=True)

    def __str__(self):
        return self.name




class Book(models.Model):
    """Contains information relating to the book."""
    title = models.CharField(max_length=50)
    book_author = models.ManyToManyField(Author, help_text="Enter the author/s of the book.")
    programming_language = models.ManyToManyField("Programming_Languages", help_text="Select the appropriate programming language", blank=True)
    description = models.TextField(max_length=1024, help_text="Enter a description of the book's topic")
    date_added = models.DateTimeField(auto_now_add=True)
    book_url = models.URLField(max_length=200, default="")
    book_slug = models.SlugField()

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args=(self.pk, ))

class Programming_Languages(models.Model):
    """Contains the programming languages used in the book."""
    language = models.CharField(max_length=50, help_text="Enter the programming language this book covers", null=True)

    def __str__(self):
        return self.language