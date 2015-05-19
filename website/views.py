from django.shortcuts import render
from .models import Movie, Projection

# Create your views here.


def index(request):
    movies = Movie.objects.all()
   # projections = Projection.objects.all()

    movie_projections = {}
    opa = []

    for movie in movies:

        bam = Projection.objects.filter(movie_id=movie.id)
        apf = list(bam)
        # a = projections.select_related(movie_id, id)
        movie_projections[movie] = bam

    print (movie_projections)

    return render(request, "index.html", locals())
