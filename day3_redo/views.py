from django.shortcuts import HttpResponse, render, redirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.views import View
from football.models import Team, Game
from exercises_app.models import Band
from django.urls import reverse
import datetime
from random import randint


# Create your views here.
def start_end(request):
    if request.method == "GET":
        try:
            start = int(request.GET.get('start'))
            end = int(request.GET.get('end'))
            values = str(list(range(start, end + 1)))
            return HttpResponse(values)
        except (TypeError, ValueError):
            return HttpResponse('Check values entered')


def width_height(request):
    if request.method == "GET":
        try:
            width = int(request.GET['width'])
            height = int(request.GET['height'])
            values = {'width': range(1, width + 1),
                      'height': range(1, height + 1)}
            return render(request, "wh.html", context=values)
        except NameError:
            return HttpResponse('Check values entered again')


def name(request):
    if request.method == "GET":
        return render(request, 'name_form.html')
    elif request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        return HttpResponse('Hello, {} {}.'.format(first_name, last_name))


class conv_temp(View):
    def get(self, request):
        return render(request, 'conv_temp.html')

    def post(self, request):
        convert = request.POST['conversion_type']
        temp = int(request.POST['temp'])
        if convert == 'celstofahr':
            value = temp * 1.8 + 32
            return HttpResponse(f"{temp} Degrees Celsius is equal to {value} Degrees Fahrenheit")
        elif convert == 'fahrtocels':
            value = (temp - 32) * 5 / 9
            return HttpResponse(f"{temp} Degrees Fahrenheit is equal to {value} Degrees Celsius")


def show_scores(request):
    if request.method == "GET":
        try:
            set_home = Team.objects.get(pk=request.session['hostteam'])
            return render(request, 'show_scores.html', context={'teams': Team.objects.all(), 'set_home': set_home})
        except KeyError:
            return render(request, 'show_scores.html', context={'teams': Team.objects.all()})
    elif request.method == "POST":
        try:
            home_team = int(request.POST['home_team'])
            away_team = int(request.POST['away_team'])
            home_score = int(request.POST['home_score'])
            away_score = int(request.POST['away_score'])
            response = HttpResponseNotFound("You can't pick two of the same team!!")
            request.session['hostteam'] = home_team
            if home_team != away_team:
                Game.objects.create(team_home_id_id=home_team, team_away_id_id=away_team, team_home_goals=home_score,
                                    team_away_goals=away_score)
                if home_score > away_score:
                    total = Team.objects.get(pk=home_team)
                    total.points += 3
                    total.save()
                elif home_score == away_score:
                    totalhome = Team.objects.get(pk=home_team)
                    totalaway = Team.objects.get(pk=away_team)
                    totalhome.points += 1
                    totalaway.points += 1
                    totalhome.save()
                    totalaway.save()
                elif away_score > home_score:
                    total = Team.objects.get(pk=away_team)
                    total.points += 3
                    total.save()
                return redirect("/games-played/?teamid={}".format(home_team))
            else:
                return response
        except ValueError:
            raise Http404


def modify_team(request):
    if request.method == "GET":
        id = int(request.GET.get('id').strip('/'))
        team = Team.objects.get(pk=id)
        return render(request, "modify_team.html", context={'id': id, 'team': team})
    if request.method == "POST":
        try:
            team = int(request.POST.get('team_id'))
            points = request.POST.get('points')
            name = request.POST.get('team_name')
            if name is not None and int(points) > 0:
                modify = Team.objects.get(pk=team)
                modify.name = name
                modify.points = points
                modify.save()
                return redirect("/league-table")
            else:
                return HttpResponse("Enter valid information to update points table!")
        except ValueError:
            return HttpResponse("Enter valid information to update points table!")
    else:
        return HttpResponse("Enter valid information to update points table!")


def test_session(request):
    request.session['thisisatest'] = 'testworked'
    return HttpResponse(f'Session = {request.session}')


def set_session_redo(request):
    request.session['counter'] = 0
    return HttpResponse(request.session.get('counter'))


def show_session_redo(request):
    try:
        request.session['counter'] += 1
        return HttpResponse(request.session.get('counter'))
    except KeyError:
        return HttpResponse("Session needs to be set first")


def delete_session_redo(request):
    del request.session['counter']
    return HttpResponse("Session has been deleted!")


def login_redo(request):
    if request.method == "GET":
        try:
            return HttpResponse('Welcome {}, you are logged in'.format(request.session['loggedUser']))
        except KeyError:
            return render(request, 'login_redo.html')
    elif request.method == "POST":
        name = request.POST.get('name')
        request.session['loggedUser'] = name
        return HttpResponse('{} has been logged on'.format(request.session['loggedUser']))


def add_to_session_redo(request):
    if request.method == "GET":
        return render(request, 'add_to_session_redo.html')
    elif request.method == "POST":
        s_key = request.POST['key']
        s_value = request.POST['value']
        request.session[s_key] = s_value
        return HttpResponse('{} session has now been registered!'.format(request.session[s_key]))


def show_all_sessions_redo(request):
    if request.method == "GET":
        pairs = request.session.items()
        return render(request, 'show_all_sessions_redo.html', context={'pairs': pairs})


def set_cookie_redo(request):
    response = HttpResponse('Cookie set!')
    response.set_cookie('User', 'Vatche')
    return response


def show_cookie_redo(request):
    value = request.COOKIES.get('User')
    return HttpResponse('User is {}'.format(value))


def delete_cookie_redo(request):
    response = HttpResponse('Cookie has been deleted!')
    response.delete_cookie('User')
    return response


def add_to_cookie_redo(request):
    if request.method == "GET":
        return render(request, 'add_to_cookie_redo.html')
    elif request.method == "POST":
        c_key = request.POST.get('key')
        c_value = request.POST.get('value')
        response = HttpResponse('Cookie has been added!')
        response.set_cookie(c_key, c_value)
        return response


def show_all_cookies_redo(request):
    if request.method == "GET":
        cookies = request.COOKIES.items()
        return render(request, 'show_all_cookies_redo.html', context={'cookies': cookies})


def set_as_favourite(request):
    if request.method == "GET":
        try:
            int_id = int(request.GET['id'].strip('/'))
            try:
                team_check = Team.objects.get(pk=int_id)
                fav_team_name = team_check.name
                response = HttpResponse('Users favourite team {}is set'.format(fav_team_name))
                year = datetime.datetime.utcnow() + datetime.timedelta(days=365)
                response.set_cookie('FavouriteTeam', fav_team_name, expires=year)
                return response
            except (ObjectDoesNotExist, AttributeError):
                raise Http404('That ID does not exist!!')
        except (AttributeError, ValueError):
            return HttpResponse('Enter a valid number in the url')


class name_view(View):
    def get(self, request):
        return render(request, 'name_view.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        return HttpResponse(f'Welcome, {first_name} {last_name}!')


class createBand(View):
    def get(self, request):
        genres = {
            -1: 'not defined',
            0: 'rock',
            1: 'metal',
            2: 'pop',
            3: 'hip-hop',
            4: 'electronic',
            5: 'reggae',
            6: 'other',
        }
        return render(request, 'create_band.html', context={'genres': genres.items()})

    def post(self, request):
        name = request.POST["name"]
        year = request.POST["year"]
        still_active = "still_active" in request.POST
        genre = int(request.POST.get("genreselect"))
        Band.objects.create(name=name, year=year, still_active=still_active, genre=genre)
        return HttpResponse(f"{name} was added to the database")


def random3(request, min_number, max_number):
    return HttpResponse(f'''<p> nim_number is : {min_number}</p>
                        <p> max_number is : {max_number}</p>
                        <p> drawn no: {randint(int(min_number), int(max_number))}</p>
                     ''')
