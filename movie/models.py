from django.db import models
from datetime import datetime

class Movie(models.Model):
	title = models.CharField(max_length=128, unique=True)
	plot = models.TextField(null=True, blank=True)
	likes = models.PositiveIntegerField(default=0)
	is_active = models.BooleanField(default=True)

	date_created = models.DateTimeField(default=datetime.now())
	date_updated = models.DateTimeField(default=datetime.now())
	date_deleted = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('movie_update', kwargs={'pk': self.pk})
