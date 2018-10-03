from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Movie

class MovieList(ListView):
	model = Movie


class MovieDetail(DetailView):
	model = Movie


class MovieAdd(CreateView):
	model = Movie
	fields = ['title', 'plot']
	success_url = reverse_lazy('movie_list')


class MovieUpdate(UpdateView):
	model = Movie
	fields = ['title', 'plot']
	success_url = reverse_lazy('movie_list')


class MovieDelete(DeleteView):
	model = MovieDetail
	success_url = reverse_lazy('movie_list')
