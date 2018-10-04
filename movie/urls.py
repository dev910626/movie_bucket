from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.MovieList.as_view(), name='list'),
    path('movie/<int:pk>/', views.MovieDetail.as_view(), name='detail'),
    path('movie/add/', views.MovieAdd.as_view(), name='add'),
    path('movie/<int:pk>/update/', views.MovieUpdate.as_view(), name='update'),
    path('movie/<int:pk>/delete/', views.MovieDelete.as_view(), name='delete'),
    path('movie/<int:pk>/like/', views.AddLike.as_view(), name='like'),
]
