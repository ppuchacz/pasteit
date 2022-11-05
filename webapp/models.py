from django.db import models

# Create your models here.
class Note(models.Model):
    contents = models.TextField()
    # author = 
    created_at = models.DateTimeField()
    format = models.TextField()
