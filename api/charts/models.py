from django.db import models

# Create your models here.
class Data(models.Model):
    movies = models.CharField(max_length=200)
    year = models.IntegerField()
    genre = models.CharField(max_length=200)
    rating = models.FloatField()
    one_line = models.CharField(max_length=200)
    stars = models.CharField(max_length=200)
    votes = models.IntegerField()
    run_time = models.CharField(max_length=200)
    gross = models.FloatField()

    def __str__(self):
    	return self.movies