from django.urls import path
from movieapp import views

urlpatterns = [
    path('form/',views.movie_form,name = 'form'),
    path('all/',views.all_movies,name = 'movies')
]