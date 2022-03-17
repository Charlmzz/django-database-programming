from django.shortcuts import render
from sql.queries import *
from sql.models import *

# Create your views here.
def display(request):
    #query 1
    flag,mins,maxs=query1()
    ans1 = Player.objects.all()
    
    if flag[0]:
        ans1 = ans1.filter(mpg__gte = mins[0], mpg__lte = maxs[0])
    if flag[1]:
        ans1 = ans1.filter(ppg__gte = mins[1], ppg__lte = maxs[1])
    if flag[2]:
        ans1 = ans1.filter(rpg__gte = mins[2], rpg__lte = maxs[2])
    if flag[3]:
        ans1 = ans1.filter(apg__gte = mins[3], apg__lte = maxs[3])
    if flag[4]:
        ans1 = ans1.filter(spg__gte = mins[4], spg__lte = maxs[4])
    if flag[5]:
        ans1 = ans1.filter(bpg__gte = mins[5], bpg__lte = maxs[5])
    

    #query 2
    color_name = query2()
    ans2 = Team.objects.filter(color_id__name=color_name)

    #query 3
    team_name=query3()
    ans3 = Player.objects.filter(team_id__name = team_name).order_by('-ppg')

    #query 4
    team_state,team_color = query4()
    ans4 = Player.objects.filter(team_id__state_id__name = team_state)
    ans4 = ans4.filter(team_id__color_id__name = team_color)

    #query 5
    wins = query5()
    ans5 = Player.objects.filter(team_id__wins__gt=wins)

    return render(request, 'sql/display.html',{"ans1":ans1,"ans2":ans2,"ans3":ans3,"ans4":ans4,"ans5":ans5})
