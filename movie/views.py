from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import *

from .classes.movie import MovieClass as m_c
from .classes.movie_detail import MovieDetailClass as md_c

class ListPage(View):
	TEMPLATE_NAME = 'movie/list.html'

	def get(self, request, *args, **kwargs):
		template_vars = {
			'movies': m_c.get_active_movies()
		}

		return render(self.request, self.TEMPLATE_NAME, template_vars)


class DetailPage(View):
	TEMPLATE_NAME = 'movie/detail.html'

	def get(self, request, *args, **kwargs):
		template_vars = {
			'movie_detail': md_c.get_movie_detail_by_movie_id(self.kwargs['movie_id'])
		}

		return render(self.request, self.TEMPLATE_NAME, template_vars)

