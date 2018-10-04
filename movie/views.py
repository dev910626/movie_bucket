from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.views import View
from django.utils.decorators import method_decorator

from .classes.session import session_decorator
from .models import Movie

@method_decorator(session_decorator, name='dispatch')
class MovieList(ListView):
	model = Movie
	queryset = Movie.objects.filter(is_active=True).order_by('title')

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['greetings'] = self.request.session['message']
		
		return context


class MovieDetail(DetailView):
	model = Movie

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['greetings'] = self.request.session['message']
		
		return context

class MovieAdd(CreateView):
	model = Movie
	fields = ['title', 'plot']
	
	def get_success_url(self):
		messages.success(self.request, self.object.title + ' successfully created!')

		return reverse('movie:detail', kwargs={'pk': self.object.id})

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['greetings'] = self.request.session['message']
		
		return context

class MovieUpdate(UpdateView):
	model = Movie
	fields = ['title', 'plot']

	def get_success_url(self):
		messages.success(self.request, self.object.title + ' successfully edited!')
		
		return reverse('movie:detail', kwargs={'pk': self.object.id})

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['greetings'] = self.request.session['message']
		
		return context

class MovieDelete(DeleteView):
	model = Movie
	
	def get_success_url(self):
		return reverse('movie:list')

	def delete(self, request, *args, **kwargs):
		movie = Movie.objects.get(pk=self.kwargs['pk'])
		movie.is_active = False
		movie.save()

		return HttpResponseRedirect('/')

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['greetings'] = self.request.session['message']
		
		return context


class AddLike(View):
	def post(self, request, *args, **kwargs):
		movie = Movie.objects.get(pk=self.kwargs['pk'])
		movie.likes += 1
		movie.save()

		return JsonResponse({'likes' : movie.likes}, content_type = 'text/plain; charset=UTF-8', safe = False)