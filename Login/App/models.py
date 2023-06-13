from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    phone = models.IntegerField(default=0)