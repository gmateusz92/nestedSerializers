from .models import Author, Book
from .serializers import AuthorSerializer, BooksSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 2
    # filter_backends = [DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'ratings']
    # filterset_fields = ['ratings']

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer