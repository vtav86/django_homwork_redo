from random import randint
from project.exercises_app.models import Band


def update_bands_without_year():
    for band in Band.objects.filter(year__isnull=True):
        band.year = randint(1990, 2000)
        band.save()


def update_bands_without_genres():
    for band in Band.objects.filter(genre=-1):
        band.genre = randint(0, 6)
        band.save()


def bands_still_active():
    for band in Band.objects.filter(still_active=False):
        band.still_active = True
        band.save()


def find_the():
    bands = []
    for band in Band.objects.filter(name__icontains="the"):
        bands.append(band)
    return bands


def find_80s():
    bands = []
    for band in Band.objects.filter(year__gte=1980, year__lt=1990, still_active=True):
        bands.append(band)
    return bands


def find_70s():
    bands = []
    for band in Band.objects.filter(year__gte=1970, year__lt=1980, name__icontains='The'):
        bands.append(band)
    return bands


def non_active_80s():
    bands = []
    for band in Band.objects.filter(year__gte=1980, year__lt=1990, still_active=False):
        bands.append(band)
    return bands


print('imported')
