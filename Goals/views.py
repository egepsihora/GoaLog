from django.shortcuts import render
from django.http import HttpResponse
from .models import Goal


# def index(request):
#     return HttpResponse("<h3>hello</h3>")


def index(request):
    goals = []
    for goal in Goal.objects.all():
        goals.append(goal.Name)
    return render(request, 'Goals/goals.html', {'goals': goals})

