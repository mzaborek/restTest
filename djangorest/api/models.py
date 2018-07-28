from _blake2 import blake2b
from django.db import models

# Create your models here.
class Movielist(models.Model):
    title = models.CharField(max_length=255, blank=False)

    year = models.CharField(max_length=15, blank=True)
    rated = models.CharField(max_length=255, blank=True)
    released = models.CharField(max_length=255, blank=True)
    runtime = models.CharField(max_length=255, blank=True)
    genre = models.CharField(max_length=255, blank=True)
    director = models.CharField(max_length=255, blank=True)
    writer = models.CharField(max_length=255, blank=True)
    actors = models.TextField(blank=True)
    plot = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    awards = models.CharField(max_length=255, blank=True)
    poster = models.CharField(max_length=255, blank=True)
    ratings = models.CharField(max_length=255, blank=True)
    metascore = models.CharField(max_length=255, blank=True)
    imdbRating = models.CharField(max_length=255, blank=True)
    imdbVotes = models.CharField(max_length=255, blank=True)
    imdbID = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)
    dvd = models.CharField(max_length=255, blank=True)
    boxoffice = models.CharField(max_length=255, blank=True)
    production = models.CharField(max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)
    season = models.CharField(max_length=31, blank=True)

    #except requests.exceptions:
    def __str__(self):
        return "{}".format(self.title)


class Comment(models.Model):
    movie = models.ForeignKey(Movielist, on_delete=models.CASCADE)
    commentText = models.TextField()
