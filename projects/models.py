from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    summary = models.TextField(max_length=200)
    url = models.URLField(default=None)

    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title
