from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

from .models import Movie

class MovieList(ListView):
	model = Movie
	queryset = Movie.objects.filter(is_active=True)


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
	
	def get_success_url(self):
		return reverse('movie:list')

	def delete(self, request, *args, **kwargs):
		movie = Movie.objects.get(pk=self.kwargs['pk'])
		movie.is_active = False
		movie.save()

		return HttpResponseRedirect('/')