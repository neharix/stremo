from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    file = models.FileField(upload_to='data/')
    preview = models.ImageField(upload_to='preview/')
    description = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.PROTECT)
    country = models.ForeignKey("Country", on_delete=models.PROTECT)
    release_time = models.DateTimeField()

    def __str__(self):
        return self.title

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name