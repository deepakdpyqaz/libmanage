from django.db import models

# Create your models here.
class Student(models.Model):
    username=models.CharField(max_length=12,primary_key=True)
    name=models.CharField(max_length=15)

    def __str__(self):
        return self.name

