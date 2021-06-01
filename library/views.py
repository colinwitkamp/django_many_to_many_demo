from django.db.models import OuterRef, Subquery, Prefetch
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer, BookListSerializer


@api_view(['GET', 'POST'])
def handle_authors(request):

    if request.method == 'GET':
        subqry = Subquery(Book.objects \
            .filter(authors=OuterRef('authors')) \
            .order_by('-published_at')[:10]
            .values_list('id', flat=True))

        authors = Author.objects.prefetch_related(
            Prefetch(
                'books',
                queryset=Book.objects.filter(id__in=subqry).distinct())).all()

        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def handle_author(request, author_id):
    if request.method == 'GET':
        try:
            subqry = Subquery(Book.objects \
                .filter(authors=OuterRef('authors')) \
                .order_by('-published_at')[:10]
                .values_list('id', flat=True))

            author = Author.objects.prefetch_related(
                Prefetch('books',
                         queryset=Book.objects.filter(
                             id__in=subqry).distinct())).get(pk=author_id)
        except Author.DoesNotExist:
            return HttpResponse(status=404)

        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    else:
        try:
            author = Author.objects.get(pk=author_id)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = AuthorSerializer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            author.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def handle_books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        
        author_name = request.query_params.get('author_name')
        if author_name is not None:
            books = books.filter(authors__name=author_name)

        author_birth_year = request.query_params.get('author_birth_year')
        if author_birth_year is not None:
            books = books.filter(authors__birth_year=author_birth_year)

        title = request.query_params.get('title')
        if title is not None:
            books = books.filter(title=title)

        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def handle_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)