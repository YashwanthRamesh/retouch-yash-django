from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.title
