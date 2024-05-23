from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=20)
    descryption=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Details(models.Model):
    name=models.CharField(max_length=20)
    age=models.CharField(max_length=20)
    place=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Car(models.Model):
    name=models.CharField(max_length=20)
    descryption=models.CharField(max_length=20)
    price=models.DecimalField (max_digits=10,decimal_places=2)

