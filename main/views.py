from django.http import HttpRequest
from django.shortcuts import redirect, render

from .models import Category, Movie


def main(request: HttpRequest):
    return render(request, "views/new_index.html")


def home(request):
    if request.method == "POST":
        try:
            request.session["query"] = request.POST["query"]
            return redirect("search")
        except:
            return redirect("home")
    else:
        movies = Movie.objects.all().order_by("-release_time")

        rows = [[]]
        i = 0
        for movie in movies:
            if len(rows[i]) == 6:
                i += 1
                rows.append([])
            rows[i].append(movie)

        context = {"categories": Category.objects.all(), "rows": rows}
        return render(request, "index.html", context)


def by_category(request, category_id):
    if request.method == "POST":
        try:
            request.session["query"] = request.POST["query"]
            return redirect("search")
        except:
            return redirect("home")
    else:
        current_category = Category.objects.get(pk=category_id)
        movies = Movie.objects.filter(category__name=current_category.name).order_by(
            "-release_time"
        )

        rows = [[]]
        i = 0
        for movie in movies:
            if len(rows[i]) == 6:
                i += 1
                rows.append([])
            rows[i].append(movie)

        context = {
            "categories": Category.objects.all(),
            "rows": rows,
            "current_category": current_category,
        }
        return render(request, "by_category.html", context)


def by_movie(request, movie_id):
    if request.method == "POST":
        try:
            request.session["query"] = request.POST["query"]
            return redirect("search")
        except:
            return redirect("home")
    else:
        movie = Movie.objects.get(pk=movie_id)

        context = {"movie": movie}
        return render(request, "by_movie.html", context)


def search(request):
    if request.session.get("query"):
        query = request.session["query"].capitalize()
        del request.session["query"]
        found_content = Movie.objects.filter(title__contains=query)

        rows = [[]]
        i = 0
        for movie in found_content:
            if len(rows[i]) == 6:
                i += 1
                rows.append([])
            rows[i].append(movie)

        return render(request, "search.html", {"rows": rows})
    else:
        if request.method == "POST":
            try:
                request.session["query"] = request.POST["query"]
                return redirect("search")
            except:
                return redirect("home")
        else:
            return redirect("home")
