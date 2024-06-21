from django.shortcuts import render
from django.http import HttpResponse
from .models import Team

def index(request):
    return HttpResponse("Young Scientist Academy")

def home(request):
    return render(request, "core/home.html", {})

def ysa(request):
    return render(request, "core/ysahome.html", {})

def leaderboard_view(request):
    teams = Team.objects.all().order_by('-total_points')
    context = {
        'teams': teams,
    }
    return render(request, 'core/leaderboard.html', context)
