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

    for i in range(2):
        index = 0
        for movie in movies:
            index += 1
            

    context = {"categories": Category.objects.all(), 'rows': rows}
    return render(request, "index.html", context)