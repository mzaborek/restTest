from django.db import models


# Create your models here.
class Movielist(models.Model):
    Title = models.CharField(max_length=255, blank=False)

    Year = models.CharField(max_length=15, blank=True)
    Rated = models.CharField(max_length=255, blank=True)
    Released = models.CharField(max_length=255, blank=True)
    Runtime = models.CharField(max_length=255, blank=True)
    Genre = models.CharField(max_length=255, blank=True)
    Director = models.CharField(max_length=255, blank=True)
    Writer = models.CharField(max_length=255, blank=True)
    Actors = models.TextField(blank=True)
    Plot = models.CharField(max_length=255, blank=True)
    Language = models.CharField(max_length=255, blank=True)
    Country = models.CharField(max_length=255, blank=True)
    Awards = models.CharField(max_length=255, blank=True)
    Poster = models.CharField(max_length=255, blank=True)
    Ratings = models.CharField(max_length=255, blank=True)
    Metascore = models.CharField(max_length=255, blank=True)
    imdbRating = models.CharField(max_length=255, blank=True)
    imdbVotes = models.CharField(max_length=255, blank=True)
    imdbID = models.CharField(max_length=255, blank=True)
    Type = models.CharField(max_length=255, blank=True)
    DVD = models.CharField(max_length=255, blank=True)
    BoxOffice = models.CharField(max_length=255, blank=True)
    Production = models.CharField(max_length=255, blank=True)
    Website = models.CharField(max_length=255, blank=True)
    totalSeasons = models.CharField(max_length=31, blank=True)

    # except requests.exceptions:
    def __str__(self):
        return "{}".format(self.Title)


class Comment(models.Model):
    movie = models.ForeignKey(Movielist, on_delete=models.CASCADE)
    commentText = models.TextField()
