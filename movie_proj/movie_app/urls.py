from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.mov, name='movies'),
    path('movies/movie_details/<int:movie_id>/', views.movie_details, name='movie_details'),
    path('movies/movie_synopsis/<int:movie_id>/', views.movie_synopsis, name='movie_synopsis'),
]