from django.urls import path
from movie.views import *

app_name = 'movie'

urlpatterns = [
    path('', ListPage.as_view(), name='list'),
    path('movie/<int:movie_id>/', DetailPage.as_view(), name='detail'),
]
