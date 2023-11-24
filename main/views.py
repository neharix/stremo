from django.shortcuts import render
from .models import Category, Movie


def home(request):

    last_id = Movie.objects.last().pk
    first_id = Movie.objects.first().pk
    second_row_bool = False

    try:
        row1 = Movie.objects.filter(pk__range=(last_id - 6, last_id))
        second_row_bool = True
    except:
        row1 = Movie.objects.filter(pk__range=(first_id, last_id))
    movies = Movie.objects.all().order_by('-created_at')

    if second_row_bool:
        try:
            row1 = Movie.objects.filter(pk__range=(last_id - 13, last - 7))
        except:
            row2 = Movie.objects.filter(pk__range=(first_id, last_id - 7))
    
    rows = [row1, row2]

    context = {"categories": Category.objects.all(), 'rows': rows}
    return render(request, "index.html", context)

def by_category(request, category_id):
    current_category = Category.objects.get(pk=category_id)
    movies = Movie.objects.filter(category__name=current_category.name).order_by('-created_at')


    rows = [[]]
    i = 0
    for movie in movies:
        if len(rows[i]) == 6:
            i += 1
            rows.append([])
        rows[i].append(movie)

    context = {"categories": Category.objects.all(), 'rows': rows, "current_category": current_category}
    return render(request, "by_category.html", context)

def by_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)

    context = {"movie": movie}
    return render(request, 'by_movie.html', context)