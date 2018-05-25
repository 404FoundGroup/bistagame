from django.db import models

# Create your models here.

# TODO: recode the User class to use the django auth system
class User(models.Model):
    email = models.EmailField()
    username = models.CharField()
    password = models.CharField()

class UserData(models.Model):
    medalList = models.CharField()
    #gameList = models.ForeignKey() -> this is represented in the game table
    frieds = models.ForeignKey() # TODO: fix this
    blocked = models.CharField()
    totalscore = models.IntegerField()
    #gamesPlayed = models.ForeignKey() -> this is represented in the game table
    winCount = models.IntegerField()
    loseCount = models.IntegerField()
    leaveCount = models.IntegerField()

class Game(models.Model):
    playerAsk = models.ForeignKey()
    playerAsn = models.ForeignKey()
    log = models.CharField()
    soreAsk = models.IntegerField()
    soreAns = models.IntegerField()