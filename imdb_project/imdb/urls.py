from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name = 'home'),
    path('home/', views.home_page, name = 'home_page'),
    path('movie/<movie_id>/', views.movie_page, name = 'movie'),
    path('actor/<actor_id>/', views.actor_page, name = 'actor'),
    path('director/<int:director_id>/', views.director_page, name = 'director'),
    path('analytics/', views.analytics_page, name = 'analytics'),
]