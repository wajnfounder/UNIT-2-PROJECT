from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_view(request: HttpRequest):
    return render(request, 'core/pages/home.html')


def about_view(request: HttpRequest):
    return render(request, 'core/pages/about.html')


def games_view(request: HttpRequest):
    return render(request, 'core/pages/games.html')


def teams_view(request: HttpRequest):
    return render(request, 'core/pages/teams.html')


def infrastructure_view(request: HttpRequest):
    return render(request, 'core/pages/infrastructure.html')


def timeline_view(request: HttpRequest):
    return render(request, 'core/pages/timeline.html')


def events_view(request: HttpRequest):
    return render(request, 'core/pages/events.html')