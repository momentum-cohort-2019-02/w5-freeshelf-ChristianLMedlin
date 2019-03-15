from django.contrib import admin

from core.models import Author, Book, Programming_Languages
# Register your models here.

admin.site.register(Author)

admin.site.register(Programming_Languages)


@admin.register(Book)
class Book(admin.ModelAdmin):
    prepopulated_fields = {"book_slug": ("title",)}