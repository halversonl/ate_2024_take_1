from django.db import models


# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateTimeField(null=True, blank=True)
    description = models.TextField()
    file = models.FileField(upload_to='uploads/')
