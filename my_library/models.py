from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
   
    email = models.EmailField()
    password = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=100, blank=True)
    note = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return f'{self.name}' 

class Author(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="authors", blank=True,null=True)
    name = models.CharField(max_length=255, blank=True)
    surname = models.CharField(max_length=255, blank=True)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.surname}' 
    

class Book(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE,   related_name="books",blank=True,null=True )
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  related_name="books", blank=True,null=True)
    name = models.CharField(max_length=255, blank=True,)
    
    explanation = models.TextField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True,blank=True, null=True)
    date_published = models.DateTimeField(blank=True, null=True)

    # def __str__(self):
    #     return f'{self.name}'      
