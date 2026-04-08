from django.urls import path
from . import views

app_name ="core"

urlpatterns = [
    path('', views.home_view, name='home'),

    path('about/', views.about_view, name='about'),

    path('games/', views.games_view, name='games'),
    path('teams/', views.teams_view, name='teams'),

    path('infrastructure/', views.infrastructure_view, name='infrastructure'),
    path('events/', views.events_view, name='events'),
    path('timeline/', views.timeline_view, name='timeline'),
]