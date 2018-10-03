from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import Movie

class MovieList(ListView):
	model = Movie


class MovieDetail(DetailView):
	model = Movie


class MovieAdd(CreateView):
	model = Movie
	fields = ['title', 'plot']
	
	def get_success_url(self):
		return reverse('movie:detail', kwargs={'pk': self.object.id})

class MovieUpdate(UpdateView):
	model = Movie
	fields = ['title', 'plot']

	def get_success_url(self):
		return reverse('movie:detail', kwargs={'pk': self.object.id})


class MovieDelete(DeleteView):
	model = Movie
	success_url = reverse_lazy('list')
