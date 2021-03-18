from django.shortcuts import render,HttpResponse
from librarian.models import Book, Issue, BookRequest
from librarian.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from student.models import Student
# Create your views here.

@api_view(["GET"])
def showavailable(request):
    try:
        bks=Book.objects.filter(available=True)
        bksSerializer = BookSerializer(bks,many=True)
        return Response(bksSerializer.data,status=200)
    except:
        return Response(status=500)

@api_view(["GET"])
def showissued(request):
    try:
        bks=Book.objects.filter(available=False)
        bksSerializer = BookSerializer(bks,many=True)
        return Response(bksSerializer.data,status=200)
    except:
        return Response(status=500)

@api_view(["POST"])
def issueBook(request):
    if(request.method=="POST"):
        student = request.data['student']
        book = request.data['book']

        try:
            stdnt = Student.objects.get(username=student)
        except:
            return Response({"Error":"Invalid student username"},status=406)
        
        try:
            bk = Book.objects.get(book_id=int(book))
            if(not(bk.available)):
                return Response({"Error":"Book not available"},status=406)
        except:
            return Response({"Error":"Book not found"},status=406)
        
        try:
            bk.available=False
            issue=Issue(book=bk,student=stdnt)
            bk.save()
            issue.save()
            return Response({"Error":False},status=200)
        except:
            return Response(status=500)

@api_view(["POST"])
def returnBook(request):
    if(request.method=="POST"):
        student = request.data['student']
        book = request.data['book']

        try:
            issue = Issue.objects.get(student__username=student,book__book_id=int(book))
            bk=issue.book
            bk.available=True
            bk.save()
            issue.delete()
            return Response({"Error":False},status=200)
        except:
            return Response({"Error":"Invalid book and student data"},status=406)

@api_view(["POST"])
def requestBook(request):
    if(request.method=="POST"):
        student = request.data['student']
        book = request.data['book']

        try:
            stdnt = Student.objects.get(username=student)
        except:
            return Response({"Error":"Invalid student username"},status=406)
        
        try:
            bk = Book.objects.get(book_id=int(book))
            if(bk.available):
                return Response({"Error":"Book is available"},status=406)
        except:
            return Response({"Error":"Book not found"},status=406)
        
        try:
            req=BookRequest(book=bk,student=stdnt)
            req.save()
            return Response({"Error":False},status=200)
        except:
            return Response(status=500)


        


