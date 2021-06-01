from django.db import models
from django.core.validators import *

class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_year = models.IntegerField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    published_at = models.DateField(auto_now=True)
    authors = models.ManyToManyField(Author, related_name='books')
