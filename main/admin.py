from django.contrib import admin
from .models import Category, Movie


admin.site.register(Movie)
admin.site.register(Category)