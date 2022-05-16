from django.shortcuts import render, HttpResponse
from football.models import Team, Game


# Create your views here.
def league_table(request):
    fav_team = request.COOKIES.get('FavouriteTeam')
    info = {'team_info': Team.objects.all().order_by('-points'), 'fav_team': fav_team}
    return render(request, "football.html", info)


def games_played(request):
    teams = {
        1: 'Piast Piastów',
        2: 'Perła Złotokłos',
        3: 'LKS Chlebnia',
        4: 'Naprzód Brwinów',
        5: 'KS Teresin',
        6: 'Józefovia Józefów',
        7: 'Okęcie Warszawa',
        8: 'Żyrardowianka Żyrardów',
        9: 'Przyszłość Włochy',
        10: 'Ryś Laski',
        11: 'SEMP Ursynów',
        12: 'Promyk Nowa Sucha',
        13: 'Świt Warszawa',
        14: 'FC Lesznowola',
        15: 'Pogoń II Grodzisk Mazowiecki',
        16: 'Milan Milanówek',
    }
    if request.method == "GET":
        if request.GET.get('teamid') is not None:
            try:
                teamid = request.GET.get('teamid')
                teamobj = Team.objects.get(pk=teamid)
                total_games = Game.objects.filter(team_home_id=teamid) | Game.objects.filter(team_away_id=teamid)
                info = {'total_games': total_games, 'teams': teams, 'teamid': teamid, 'teamobj':teamobj}
                return render(request, "games_played.html", info)
            except ValueError:
                return HttpResponse('Team ID needs to be a valid number')
        else:
            total_games = Game.objects.filter(team_home_id=1) | Game.objects.filter(team_away_id=1)
            info = {'total_games': total_games, 'teams': teams}
            return render(request, "games_played.html", info)

