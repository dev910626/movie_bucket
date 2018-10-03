from django.db import models
from datetime import datetime

class Movie(models.Model):
	title = models.CharField(max_length=128, unique=True)
	is_active = models.BooleanField(default=True)

	date_created = models.DateTimeField(default=datetime.now())
	date_updated = models.DateTimeField(default=datetime.now())
	date_deleted = models.DateTimeField(null=True, blank=True)


class MovieDetails(models.Model):
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	plot = models.TextField()
	likes = models.PositiveIntegerField(default=0)

	date_created = models.DateTimeField(default=datetime.now())
	date_updated = models.DateTimeField(default=datetime.now())
	date_deleted = models.DateTimeField(null=True, blank=True)


class MovieEditHistory(models.Model):
	editor = models.CharField(max_length=64)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

	date_created = models.DateTimeField(default=datetime.now())
	date_updated = models.DateTimeField(default=datetime.now())
	date_deleted = models.DateTimeField(null=True, blank=True)
