from django.db import models

class Studyprogram(models.Model):
    first_name=models.CharField(max_length=90,null=True)
    choicess=[('Male','Male'),('Female','Female'),('Others','Others')]
    gender=models.CharField(max_length=10,choices=choicess)
    age=models.IntegerField(null=True)
    email=models.CharField(max_length=50,null=True)
    passwd=models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.first_name

class info(models.Model):
    name=models.CharField(max_length=100)
    Sports=models.CharField(max_length=100)
    Hobbies=models.CharField(max_length=100)
    

# Create your models here.
