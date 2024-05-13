from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=23)
    specialization = models.CharField(max_length=300)
    img = models.ImageField(upload_to='images/')