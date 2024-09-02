from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("category/<int:category_id>/", views.by_category),
    path("movie/<int:movie_id>/", views.by_movie),
    path("result/", views.search, name="search"),
    path("new/", views.main),
]
