from django.contrib import admin
from librarian.models import Book, Issue, BookRequest
# Register your models here.

admin.site.register(Book)
admin.site.register(Issue)
admin.site.register(BookRequest)
