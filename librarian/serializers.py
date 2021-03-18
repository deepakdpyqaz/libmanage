from rest_framework import serializers
from librarian.models import Book, Issue, BookRequest
from student.serializers import StudentSerializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields=["book_id","name"]

class IssueSerializer(serializers.Serializer):
    student=StudentSerializer()
    book=BookSerializer()

class BookRequestSerializer(serializers.Serializer):
    student=StudentSerializer()
    book=BookSerializer()

