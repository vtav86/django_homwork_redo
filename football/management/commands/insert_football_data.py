from django.core.management import BaseCommand

from football.management.commands_data.football_data import GAMES_DATA, TEAMS_DATA
from football.models import Game, Team


def insert_teams():
    for name, points in TEAMS_DATA:
        Team.objects.create(name=name, points=points)


def insert_games():
    for team_home_id, team_home_goals, team_away_id, team_away_goals in GAMES_DATA:
        Game.objects.create(team_home_id=team_home_id, team_home_goals=team_home_goals,
                            team_away_id=team_away_id, team_away_goals=team_away_goals)


class Command(BaseCommand):
    help = "Insert data about football league to data base."

    def handle(self, *args, **kwargs):
        insert_teams()
        insert_games()
        print("Data load successfully!")
