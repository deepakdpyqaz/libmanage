from django.db import models
from student.models import Student
# Create your models here.
class Book(models.Model):
    book_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    available=models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Issue(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)

    def __str__(self):
        return self.book.name


class BookRequest(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)

    def __str__(self):
        return self.book.name