from _blake2 import blake2b
from django.db import models

# Create your models here.
class Movielist(models.Model):
    title = models.CharField(max_length=255, blank=False)


    year = models.CharField(max_length=15, blank=True)
    runtime = models.CharField(max_length=255, blank=True)
    released = models.CharField(max_length=255, blank=True)
    actors = models.TextField(blank=True)
    season = models.CharField(max_length=31, blank=True)

    #except requests.exceptions:
    def __str__(self):
        return "{}".format(self.title)


class Comment(models.Model):
    movie = models.ForeignKey(Movielist, on_delete=models.CASCADE)
    commentText = models.TextField()
