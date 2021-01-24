from django.db import models


class Todo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


class Books(models.Model):
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=50)
    description=models.TextField()
    price=models.IntegerField()
    genre=models.CharField(max_length=50)
    author=models.CharField(max_length=100)
    year=models.DateField()
    
    # Create your models here.
