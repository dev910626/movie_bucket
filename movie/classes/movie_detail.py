from ..models import Movie, MovieDetail


class MovieDetailClass:
	@staticmethod
	def get_movie_detail_by_movie_id(movie_id):
		movie = Movie.objects.get(pk=movie_id)

		return MovieDetail.objects.get(movie=movie)