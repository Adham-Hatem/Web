from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, default="")
    author = models.CharField(max_length=30, default="")
    cover = models.ImageField(upload_to='book_covers/')

    def __str__(self):
        return self.title