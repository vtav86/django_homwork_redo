from django.shortcuts import render, HttpResponse
from homework_redo.models import Movie, Person


# Create your views here.
def movies(request):
    if request.method == "GET":
        if 'sorted' not in request.session.keys():
            movie_list = Movie.objects.all().order_by('-year')
            return render(request, 'homework_app/movies.html', {'movies': movie_list})
        else:
            if request.session['sorted'] == 1:
                movie_list = Movie.objects.all().order_by('-rating')
                return render(request, 'homework_app/movies.html', {'movies': movie_list})
            elif request.session['sorted'] == 2:
                movie_list = Movie.objects.all().order_by('rating')
                return render(request, 'homework_app/movies.html', {'movies': movie_list})
            elif request.session['sorted'] == 0:
                movie_list = Movie.objects.all().order_by('-year')
                return render(request, 'homework_app/movies.html', {'movies': movie_list})
    elif request.method == "POST":
        if request.POST.get('ratedown'):
            movie_list = Movie.objects.all().order_by('-rating')
            request.session['sorted'] = 1
            return render(request, 'homework_app/movies.html', {'movies': movie_list})
        elif request.POST.get("rateup"):
            movie_list = Movie.objects.all().order_by('rating')
            request.session['sorted'] = 2
            return render(request, 'homework_app/movies.html', {'movies': movie_list})
        elif request.POST.get("default"):
            movie_list = Movie.objects.all().order_by('-year')
            request.session['sorted'] = 0
            return render(request, 'homework_app/movies.html', {'movies': movie_list})


def movie_details(request, id):
    movie = Movie.objects.get(pk=id)
    return HttpResponse(f"""Movie is {movie.title}.
    It was produced in {movie.year} and directed by {movie.director}.
    It stars {movie.actors}.""")


def persons(request):
    person = Person.objects.all()
    return render(request, 'homework_app/persons.html', context={'persons': person})


def edit_person(request, id):
    if request.method == "GET":
        person = Person.objects.get(pk=id)
        return render(request, 'homework_app/edit-person.html', context={'person': person})
    elif request.method == "POST":
        person = Person.objects.get(pk=id)
        person.first_name = request.POST.get("first_name")
        person.last_name = request.POST.get("last_name")
        person.save()
        return HttpResponse(f"Name edited to {person.first_name} {person.last_name}")


def add_person(request):
    if request.method == "GET":
        return render(request, 'homework_app/add-person.html')
    elif request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        Person.objects.create(first_name=first_name, last_name=last_name)
        return HttpResponse(f"Name {first_name} {last_name} added to database")


def edit_movie(request, id):
    if request.method == "GET":
        info = Movie.objects.get(pk=id)
        return render(request, "homework_app/edit-movie.html", context={'info': info})
    elif request.method == "POST":
        movie_id = request.POST.get("movie_id")
        movie = Movie.objects.get(pk=movie_id)
        movie.title = request.POST.get("title")
        movie.year = request.POST.get("year")
        movie.rating = request.POST.get("rating")
        director = Person.objects.get(pk=movie.director_id)
        screenplay = Person.objects.get(pk=movie.screenplay_id)
        director.director = request.POST.get("director")
        screenplay.screenplay = request.POST.get("writer")
        movie.save()
        director.save()
        screenplay.save()
        return HttpResponse(f"Movie {movie.title} has been edited")


def add_movie(request):
    if request.method == "GET":
        people = Person.objects.all()
        return render(request, 'homework_app/add-movie.html', context={'people': people})
    elif request.method == "POST":
        director = request.POST.get("director")
        screenplay = request.POST.get("writer")
        directorobject = Person.objects.get(id=director)
        screenplayobject = Person.objects.get(id=screenplay)

        title = request.POST.get("title")
        year = request.POST.get("year")
        rating = request.POST.get("rating")
        Movie.objects.create(title=title, year=year, rating=rating, director=directorobject,
                             screenplay=screenplayobject)

        return HttpResponse(f"Movie {title} added to database")


def search_movie(request):
    if request.method == "GET":
        return render(request, 'homework_app/search_movie.html')
    elif request.method == "POST":
        movie_terms = {}
        person_terms = {}
        s_title = request.POST.get('title').lower()
        s_first_name = request.POST.get('first_name').lower()
        s_last_name = request.POST.get('last_name').lower()
        s_year_from = (request.POST.get('year_from'))
        s_year_to = (request.POST.get('year_to'))
        s_genre = request.POST.get('genre').lower()
        s_rating_from = (request.POST.get('rating_from'))
        s_rating_to = (request.POST.get('rating_to'))
        if s_title and len(s_title) >= 1:
            movie_terms["title__icontains"] = s_title
        if s_first_name and len(s_first_name) >= 1:
            person_terms["first_name__icontains"] = s_first_name
        if s_last_name and len(s_last_name) >= 1:
            person_terms["last_name__icontains"] = s_last_name
        if s_year_from and len(s_year_from) >= 1:
            movie_terms["year__gte"] = int(s_year_from)
        if s_year_to and len(s_year_to) >= 1:
            movie_terms["year__lte"] = int(s_year_to)
        if s_genre and len(s_genre) >= 1:
            movie_terms["genre__icontains"] = s_genre
        if s_rating_to and len(s_rating_to) >= 1:
            movie_terms["rating__lte"] = int(s_rating_to)
        if s_rating_from and len(s_rating_from) >= 1:
            movie_terms["rating__gte"] = int(s_rating_from)
        movie_results = Movie.objects.filter(**movie_terms)
        person_results = Person.objects.filter(**person_terms)
        return render(request, "homework_app/search_movie.html",
                      context={'mresults': movie_results, 'presults': person_results})
        # Code works fine up to here

        # I removed the below code from out of above view.
        # I was trying to search using Person model terms (first_name last_name)
        # Then comparing screenplay/director ids from both Models.
        # PLEASE NOTE MY CODE BELOW IS A MESS, I WAS JUST DOING TRIAL AND ERROR
        # I also realised I will need to have an OR in the filter for the screenplay and director search terms

        # moviedb_name_ids = []
        # for each_person in movie_results:
        #     moviedb_name_ids.append(str(each_person.director_id).split(','))
        #     moviedb_name_ids.append(str(each_person.screenplay_id).split(','))
        # persondb_name_ids = []
        # for each_person in person_results:
        #     persondb_name_ids.append(str(each_person.id).split(','))
        # compare = []
        # for each_id1 in moviedb_name_ids:
        #     if each_id1 in persondb_name_ids:
        #         compare.append(each_id1)
        # final_result = []
        # for each_id in compare:
        #     for each in each_id:
        #         movie_terms['screenplay_id'] = each
        #         movie_terms['director_id'] = each
        #         final_result.append(Movie.objects.filter(**movie_terms))
