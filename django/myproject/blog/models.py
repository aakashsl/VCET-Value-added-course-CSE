from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField("Author", max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    heading = models.CharField("Heading", max_length=50)
    content = models.CharField("Content", max_length=1000)
    author = models.ForeignKey(Author, related_name='posts', on_delete=models.CASCADE)

