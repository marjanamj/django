
from django.db import models
from django.contrib import admin

class Books(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=256)
    owner = models.CharField() 

    def __str__(self):
        return self.title