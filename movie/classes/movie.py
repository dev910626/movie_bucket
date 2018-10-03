from ..models import Movie
class MovieClass:
	@staticmethod
	def get_movie_by_id(movie_id):
		return Movie.objects.get(pk=movie_id)

	@staticmethod
	def get_active_movies():
		return Movie.objects.filter(is_active=True).order_by('title')
		