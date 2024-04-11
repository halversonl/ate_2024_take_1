from django.db import models


# Create your models here.
class Activity(models.Model):
    title = models.TextField()
    date = models.TextField()
    description = models.TextField()
    file = models.FileField()
