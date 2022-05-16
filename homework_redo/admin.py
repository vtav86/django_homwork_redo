from django.contrib import admin
from homework_redo.models import *
# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(PersonMovie)