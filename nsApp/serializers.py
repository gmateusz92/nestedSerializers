from .models import Author, Book
from rest_framework import serializers

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    books = BooksSerializer(read_only = True, many = True)
    class Meta:
        model = Author
        fields = '__all__'        