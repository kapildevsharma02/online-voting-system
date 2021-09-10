from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class VotingList(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None, unique=True)
    vote = models.CharField(max_length=300)
    status = models.BooleanField(default = True)

    def __str__(self):
        return self.vote + " - " + str(self.status)

class Results(models.Model):
    candidate = models.CharField(max_length=300, primary_key=True)
    votes = models.IntegerField()

    def __str__(self):
        return self.candidate + " - " + str(self.votes)

