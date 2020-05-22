from django.db import models

# Create your models here.
class Signup(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    streetno = models.CharField(max_length=50)
    postalcode = models.CharField(max_length=50)

class Diry(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()