from django.db import models

# Create your models here.

class School(models.Model):
    sname = models.CharField(max_length=100)
    sage = models.IntegerField()
    spawd = models.CharField(max_length=100)
    sgen = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.sname
    
    
