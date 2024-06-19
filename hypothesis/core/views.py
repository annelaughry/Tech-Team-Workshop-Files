from django.shortcuts import render
from django.http import HttpResponse
from .models import Team

def index(request):
    return HttpResponse("Young Scientist Academy")

def home(response):
    return render(response, "core/home.html", {})

def ysa(response):
    return render(response, "core/ysahome.html", {})

def leaderboard_view(request):
    teams = Team.objects.all().order_by('-total_points')
    context = {'teams': teams}
    return render(request, "core/leaderboard.html", context)


