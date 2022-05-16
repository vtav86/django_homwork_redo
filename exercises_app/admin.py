from django.contrib import admin
from exercises_app.models import Band, Category, Article, Album, AllSongs, Position, Person
# Register your models here.
admin.site.register(Band)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Album)
admin.site.register(AllSongs)
admin.site.register(Person)
admin.site.register(Position)
