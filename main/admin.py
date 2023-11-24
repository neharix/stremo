from django.contrib import admin
from .models import Category, Movie, Country


admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Country)