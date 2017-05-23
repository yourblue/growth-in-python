from django.db import models

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)