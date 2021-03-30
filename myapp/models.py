from django.db import models

# Create your models here.
class Signup(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=30)
    release_date=models.DateField()

class Python(models.Model):
    session=models.CharField(max_length=40,unique=True)
    def __str__(self):
        return self.session

class Student(models.Model):
    name=models.CharField(max_length=30, unique=False)
    session=models.ForeignKey("Python", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Contactinfo(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    address=models.CharField(max_length=30)

    class Meta:
        abstract=True

class Customer(Contactinfo):
    phone=models.CharField(max_length=30)

class Staff(Contactinfo):
    position=models.CharField(max_length=30)

class Place(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Restaurant(Place):
    italian=models.BooleanField(default=False)
    chinese=models.BooleanField(default=False)

    def __str__(self):
        return self.italian
