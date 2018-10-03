from django.urls import path
from movie.views import ListPage

app_name = 'movie'

urlpatterns = [
    path('', ListPage.as_view(), name='list'),
]
