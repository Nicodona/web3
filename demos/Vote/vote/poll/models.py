from django.db import models

class Registration(models.Model):
    figerprint = models.CharField(primary_key=True, max_length=256)
    name = models.CharField(max_length=20)
    center = models.CharField(max_length=40)
    Nid = models.IntegerField()
    Rid = models.CharField(max_length=32, null=True, blank=True) #blockchain to return an encrypted harshed private key mapping to fingerprint id


class Candidates(models.Model):
    color = models.CharField(max_length=12, primary_key=True)
    candidate_name = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)

class Poll(models.Model):
    voter = models.ForeignKey(Registration, on_delete=models.CASCADE)
    choice = models.ForeignKey(Candidates, on_delete=models.CASCADE)
    poll_harsh = models.CharField(max_length=256)   #from blockchain to return
    