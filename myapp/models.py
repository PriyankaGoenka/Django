from django.db import models

# Create your models here.
class Signup(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=30)
    release_date=models.DateField()