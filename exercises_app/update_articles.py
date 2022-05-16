import csv
from exercises_app.models import Article, Category


def update_article():
    with open(
            "/home/vatche/Documents/CodersLab/GitHub/Django_basics_homework_redo/ONL_PYT_P_02_django_basics/project"
            "/articles.csv") as file:
        each_read = csv.reader(file)
        for row in each_read:
            Article.objects.create(
                title=row[0],
                author=row[1],
                status=row[3],
                publish_date=row[4],
                removal_date=row[5])
            print(row)


def update_category():
    with open(
            "/home/vatche/Documents/CodersLab/GitHub/Django_basics_homework_redo/ONL_PYT_P_02_django_basics/project"
            "/cat.csv") as file:
        each_read = csv.reader(file)
        for row in each_read:
            Category.objects.create(
                name=row[0],
                description=row[1])
            print(row)
