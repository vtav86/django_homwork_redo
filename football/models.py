from django.db import models

class Team(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    points = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    id = models.BigAutoField(primary_key=True)
    team_home_id = models.ForeignKey('Team', blank=True, null=True, related_name='games_home', on_delete=models.CASCADE)
    team_home_goals = models.BigIntegerField(blank=True, null=True)
    team_away_id = models.ForeignKey('Team', blank=True, null=True, related_name='games_away', on_delete=models.CASCADE)
    team_away_goals = models.BigIntegerField(blank=True, null=True)


    @property
    def team_name(self):
        team_name = Team.objects.get(pk=self.team_home_id)
        return team_name



