from django.shortcuts import render
from django.http import HttpResponse
from .utils import *
from .models import *
# Create your views here.

def home_page(request):
     if request.method == 'POST':
          id = request.POST.get('delete')
          movie = Movie.objects.get(movie_id = id)
          movie.delete()
     movies_list = Movie.objects.all()
     context = {
          'movies_list': movies_list
     }
     return render(request, 'imdb_home.html', context)

def movie_page(request, movie_id):

     actors_with_roles = []
     movie = Movie.objects.get(movie_id=movie_id)
     actors = Actor.objects.filter(movies=movie).distinct()
     for actor in actors:
          actor_roles = {}
          actor_roles['actor'] = actor
          cast = Cast.objects.filter(actor=actor, movie=movie)
          actor_roles['cast_list'] = cast
          actors_with_roles.append(actor_roles)
     context = {
          'movie': movie,
          'actors': actors_with_roles
     } 
     return render(request, 'imdb_movie.html', context)

def actor_page(request, actor_id):

     actor = Actor.objects.get(actor_id=actor_id)
     cast = Cast.objects.filter(actor=actor)
     context = {
          'actor': actor,
          'movies': cast
     } 
     return render(request, 'imdb_actor.html', context)

def director_page(request, director_id):

     director = Director.objects.get(id=director_id)
     movies = director.movie_set.all()
     context = {
          'director': director,
          'movies': movies
     } 
     return render(request, 'imdb_director.html', context)

def analytics_page(request):
     data = get_imdb_multi_line_plot_with_area_data()
     data.update(get_imdb_multi_line_plot_data())
     data.update(get_imdb_two_bar_plot_data())
     data.update(single_imdb_bar_chart_data_one())
     data.update(get_imdb_polar_chart_data())
     return render(request, 'analytics.html', data)
