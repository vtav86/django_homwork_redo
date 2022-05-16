from django.db import models


# Create your models here.
class Band(models.Model):
    GENRES = (
        (-1, 'not defined'),
        (0, 'rock'),
        (1, 'metal'),
        (2, 'pop'),
        (3, 'hip-hop'),
        (4, 'electronic'),
        (5, 'reggae'),
        (6, 'other'),
    )
    name = models.CharField(max_length=64)
    year = models.IntegerField(null=True)
    still_active = models.BooleanField(default=True)
    genre = models.IntegerField(choices=GENRES, default=-1)

    def __str__(self):
        return f'Band name: {self.name}'


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)


class StatusChoices(models.IntegerChoices):
    IN_WRITING = 1, "in writing"
    PENDING_APPROVAL = 2, "pending editor approval"
    PUBLISH = 3, "published"


class Article(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64, null=True)
    content = models.TextField
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=StatusChoices.choices)
    publish_date = models.DateField(null=True)
    removal_date = models.DateField(null=True)
    category = models.ManyToManyField(Category)


class RatingChoices(models.IntegerChoices):
    ZERO = 0, ""
    ONE = 1, "⭐"
    TWO = 2, "⭐⭐"
    THREE = 3, "⭐⭐⭐"
    FOUR = 4, "⭐⭐⭐⭐"
    FIVE = 5, "⭐⭐⭐⭐⭐"


class Album(models.Model):
    album_title = models.CharField(max_length=30, null=False)
    release_year = models.IntegerField(null=True)
    rating = models.IntegerField(choices=RatingChoices.choices)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        band_name = self.band.name if self.band else "None"
        return f"Album(title='{self.album_title}', band={band_name})"


class AllSongs(models.Model):
    title = models.CharField(max_length=128)
    duration = models.TimeField(null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Songs'

    def __str__(self):
        return f"Song(title={self.title})"


class Person(models.Model):
    name = models.CharField(max_length=128)
    #position = models.OneToOneField(Position, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.name


class Position(models.Model):
    position_name = models.CharField(max_length=60)
    salary = models.IntegerField(null=True)
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.position_name
