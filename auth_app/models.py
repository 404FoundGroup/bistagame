from django.db import models

# Create your models here.

# TODO: recode the User class to use the django auth system
class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

    def get_friends(self):
        return Friendship.objects.filter(creator=self.username)

    def __str__(self):
        return self.username

class Medal(models.Model):
    name = models.CharField(max_length=64)

class UserData(models.Model):
    user = models.OneToOneField(User,models.CASCADE)
    medal = models.ManyToManyField(Medal)
    totalscore = models.IntegerField()
    winCount = models.IntegerField()
    loseCount = models.IntegerField()
    leaveCount = models.IntegerField()

class Friendship(models.Model):
    creator = models.ForeignKey(User,models.CASCADE,related_name="friends_set")
    friend = models.ForeignKey(User,models.CASCADE)
    blocked = models.BooleanField(default=False)# relation is in blocked or firend state

def get_deleted_user():
    """
        get a refrence to a deleted user
    """
    return User.objects.get_or_create(username='deleted user')[0]

class GameLog(models.Model):
    playerAsk = models.ForeignKey(User,models.SET(get_deleted_user),related_name='gamelog_asker_set')
    playerAsn = models.ForeignKey(User,models.SET(get_deleted_user),related_name='gamelog_answerer_set')
    log = models.TextField()
    scoreAsk = models.IntegerField()
    scoreAns = models.IntegerField()