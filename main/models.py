from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    file = models.FileField(upload_to='data/')
    preview = models.ImageField(upload_to='preview/')
    description = models.CharField(max_length=200)
    category = models.ForeignKey("Category", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name