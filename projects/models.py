from django.db import models


class Project(models.Model):
    title = models.TextField(max_length=20)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
