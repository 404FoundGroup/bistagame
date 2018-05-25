from django.db import models

# Create your models here.

# TODO: recode the User class to use the django auth system
class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

class Medal(models.Model):
    name = models.CharField(max_length=64)

class UserData(models.Model):
    medal = models.ManyToManyField(Medal)
    totalscore = models.IntegerField()
    winCount = models.IntegerField()
    loseCount = models.IntegerField()
    leaveCount = models.IntegerField()

class Friendship(models.Model):
    user = models.ForeignKey(User)
    friend = models.ForeignKey(User)
    blocked = models.BooleanField() # relation is in blocked or firend state

class Game(models.Model):
    playerAsk = models.ForeignKey(User)
    playerAsn = models.ForeignKey(User)
    log = models.TextField()
    scoreAsk = models.IntegerField()
    scoreAns = models.IntegerField()