from django.db import models

# Create your models here.
class Book(models.Model):
    book_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    available=models.BooleanField(default=True)
    def __str__(self):
        return self.name