from django.db import models

# Create your models here.


class Note(models.Model):
    noteTitle = models.CharField(max_length=255)
    noteDesc = models.TextField(max_length=1000)
