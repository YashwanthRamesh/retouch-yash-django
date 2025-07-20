from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': ['Top Gun', 'Inception', 'The Matrix', 'Interstellar']
}

def movies(request):
    return render(request, 'movies/movies.html', data)
    # return HttpResponse("List of movies")
    
def home(request):
    return HttpResponse("Welcome to the Movies Home Page")