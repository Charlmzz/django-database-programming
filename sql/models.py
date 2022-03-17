from django.db import models

# Create your models here.
class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, null=False)

class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, null=False)

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="name",max_length=256, null=False)
    state_id = models.ForeignKey(to="State", to_field="state_id", on_delete=models.CASCADE)
    color_id = models.ForeignKey(to="Color", to_field="color_id", on_delete=models.CASCADE)
    wins = models.IntegerField()
    losses = models.IntegerField()

class Player(models.Model):
    player_id = models.AutoField(verbose_name="player_id", primary_key=True)
    team_id = models.ForeignKey(to="Team",to_field="team_id", on_delete=models.CASCADE)
    uniform_num = models.IntegerField(verbose_name="uniform_num")
    first_name = models.CharField(verbose_name="first_name", max_length=256, null=False)
    last_name = models.CharField(verbose_name="last_name", max_length=256, null=False)
    mpg = models.IntegerField(verbose_name="mpg")
    ppg = models.IntegerField(verbose_name="ppg")
    rpg = models.IntegerField(verbose_name="rpg")
    apg = models.IntegerField(verbose_name="apg")
    spg = models.FloatField(verbose_name="spg")
    bpg = models.FloatField(verbose_name="bpg")