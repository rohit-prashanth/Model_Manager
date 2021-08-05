from django.db import models

# Create your models here.

class A(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(max_length=20)
    address = models.TextField()
    abc = models.Manager()




