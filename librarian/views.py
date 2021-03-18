from django.shortcuts import render, HttpResponse
from librarian.models import Book, Issue, BookRequest
from librarian.serializers import BookSerializer, IssueSerializer, BookRequestSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def showall(request):
    try:
        books = Book.objects.filter().all()
        bookser = BookSerializer(books,many=True)
        return Response(bookser.data,status=200)
    except:
        return Response(status=500)

@api_view(["GET"])
def showavailable(request):
    try:
        books=Book.objects.filter(available=True)
        bookser = BookSerializer(books,many=True)
        return Response(bookser.data,status=200)
    except:
        return Response(status=500)

@api_view(["GET"])
def showissued(request):
    try: 
        issues=Issue.objects.filter().all()
        issueSerializer = IssueSerializer(issues,many=True)
        return Response(issueSerializer.data,status=200)
    except:
        return Response(status=500)

@api_view(["GET"])
def showrequest(request):
    try: 
        req=BookRequest.objects.filter().all()
        reqSerializer = BookRequestSerializer(req,many=True)
        return Response(reqSerializer.data,status=200)
    except:
        return Response(status=500)
    