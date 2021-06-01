from rest_framework import serializers
from .models import Author, Book

class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'birth_year')

class BookListSerializer(serializers.ModelSerializer):
    authors = BookAuthorSerializer(read_only=True, many=True)
    class Meta:
        model = Book
        fields = ('id', 'title', 'published_at', 'authors')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'published_at', 'authors')

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only=True, many=True)
    
    class Meta:
        model = Author
        fields = ('id', 'name', 'birth_year', 'books')