from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.MovieList.as_view(), name='movie_list'),
    path('movie/<int:pk>', views.MovieDetail.as_view(), name='movie_detail'),
    path('movie/add', views.MovieAdd.as_view(), name='movie_add'),
    path('movie/<int:pk>/update', views.MovieUpdate.as_view(), name='movie_update'),
    path('movie/<int:pk>/delete', views.MovieDelete.as_view(), name='movie_delete'),
]
