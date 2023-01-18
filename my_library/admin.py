from django.contrib import admin
 
from my_library.models import Author, Category, Book, User
# Register your models here.
admin.site.register(Book)
admin.site.register(User)
admin.site.register(Author)
admin.site.register(Category)