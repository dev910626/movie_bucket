from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


from .models import *

class ListPage(View):
	TEMPLATE_NAME = 'list_page.html'

	def get(self, request, *args, **kwargs):
		movies = Movie.objects.filter(is_active=True)

		return render(self.request, self.TEMPLATE_NAME, {'movies': movies})


class DetailPage(View):
	TEMPLATE_NAME = 'detail_page.html'

	def __init__(self, movie_id):
		self.movie = Movie.objects.filter(pk=movie_id)

	def get(self, request, *args, **kwargs):
		movie_detail = MovieDetail.objects.filter(movie=self.movie)

		return render(self.request, self.TEMPLATE_NAME, {'movie_detail': movie_detail})

