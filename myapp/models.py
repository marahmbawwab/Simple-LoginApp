from django.db import models

# Create your models here.


class User_Details(models.Model):
    username = models.CharField(max_length=100, unique=True)
    Password = models.CharField(max_length=40, unique=True)
    email = models.CharField(max_length=100, unique=True)
