from django.shortcuts import render,redirect
from movieapp.forms import MovieForm
from movieapp.models import MovieModel 
# Create your views here.

# CREATE
def movie_form(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies')
    return render(request,'form.html',{'form':form})

# READ
def all_movies(request):
    movies = MovieModel.objects.all()
    return render(request,'movies.html',{'movies':movies})

