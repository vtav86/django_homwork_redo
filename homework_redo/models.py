from django.db import models


# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return self.last_name


class Genre(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='movie_director')
    screenplay = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='movie_screenplay')
    starring = models.ManyToManyField(Person, through="PersonMovie")
    year = models.IntegerField(null=False, default=1999)
    rating = models.FloatField(null=False, default=5.0)
    genre = models.ManyToManyField(Genre)

    @property
    def actors(self):
        return ','.join(actor.last_name for actor in self.starring.all())

    def __str__(self):
        return self.title


class PersonMovie(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.role} by {self.person}"
