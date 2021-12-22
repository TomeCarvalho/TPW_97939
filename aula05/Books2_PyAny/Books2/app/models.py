from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()

    @property
    def books(self):
        return Book.objects.filter(authors=self.id)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=70)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField()

    @property
    def authors(self):
        return Author.objects.filter(book__publisher=self.id).distinct()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
