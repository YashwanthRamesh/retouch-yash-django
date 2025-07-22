from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm

data = {
    'movies': ['Top Gun', 'Inception', 'The Matrix', 'Interstellar']
}

def movies(request):
    return render(request, 'movies/movies.html', data)
    # return HttpResponse("List of movies")
    
def home(request):
    return HttpResponse("Welcome to the Movies Home Page") 



# Read - List
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

# Create
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form})

# Update
def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie_form.html', {'form': form})

# Delete
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})
