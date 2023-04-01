from django.db import models

class Post(models.Model):
    username= models.CharField(max_length=300, unique=True)
    password= models.CharField(max_length=300, unique=True)
    password2= models.CharField(max_length=300, unique=True)
    email= models.CharField(max_length=300, unique=True)
    first_name= models.CharField(max_length=300, unique=True)
    last_name= models.CharField(max_length=300, unique=True)
    content= models.TextField()
