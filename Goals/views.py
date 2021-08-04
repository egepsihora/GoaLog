from django.shortcuts import render
from .models import Goal


def goal_list(request):
    goals = Goal
    return render(request, 'list.html', {'goals': goals})
