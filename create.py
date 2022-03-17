#this refers to the main.cpp for hw4
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

from sql.models import *

def add_color():
    f = open("color.txt")
    for line in f:
        color_id,name=line.split(' ')
        Color.objects.get_or_create(name=name[:-1])
    f.close()

def add_state():
    f = open("state.txt")
    for line in f:
        state_id,name=line.split(' ')
        State.objects.get_or_create(name=name[:-1])
    f.close()

def add_team():
    f = open("team.txt")
    for line in f:
        team_id,name,state_id,color_id,wins,losses=line.split(' ')
        Team.objects.get_or_create(name=name,state_id=State.objects.get(state_id=state_id),color_id=Color.objects.get(color_id=color_id),wins=wins,losses=losses)
    f.close()

def add_player():
    f = open("player.txt")
    for line in f:
        player_id,team_id,uniform_num,first_name,last_name,mpg,ppg,rpg,apg,spg,bpg=line.split(' ')
        Player.objects.get_or_create(team_id=Team.objects.get(team_id=team_id),uniform_num=uniform_num,first_name=first_name,last_name=last_name,mpg=mpg,ppg=ppg,rpg=rpg,apg=apg,spg=spg,bpg=bpg)
    f.close()

if __name__ == "__main__":
    add_color()
    add_state()
    add_team()
    add_player()
    print("finished")