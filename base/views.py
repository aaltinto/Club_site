from django.shortcuts import render, get_object_or_404
from . import models
from django.db.models import Q

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    series = models.Serie.objects.filter(
        Q(category__name__icontains=q) |
        Q(name__icontains=q) |
        Q(production_date__icontains=q)
        ).distinct()
    if not series:
        series = models.Serie.objects.all()
    vars = {
        'series': series,
        }
    return render(request, 'base/home.html', vars)

def serie(request, serie):
    serie_obj = get_object_or_404(models.Serie, name=serie)
    seasons =  models.Season.objects.filter(serie=serie_obj)
    seasons_with_episodes = [(season, season.seasonNumber.all()) for season in seasons]

    vars = {
        'serie': serie_obj,
        'seasons_with_episodes': seasons_with_episodes,
    }
    return render(request, 'base/series.html', vars)

def watch(request, serie, season, number):
    serie_obj = get_object_or_404(models.Serie, name=serie)
    seasons_obj= get_object_or_404(models.Season, serie=serie_obj, number=season)
    episode =get_object_or_404(models.Episode, season=seasons_obj, number=number)
    next_episode = None
    previous_episode = None
    if (models.Episode.objects.filter(season=seasons_obj, number=(number + 1)).exists()):
        next_episode = models.Episode.objects.filter(season=seasons_obj, number=(number + 1)).first()
    if not next_episode:
        if models.Season.objects.filter(serie=serie_obj, number=season + 1).exists(): 
            next_season =models.Season.objects.filter(serie=serie_obj, number=season + 1).first()
            next_episode = models.Episode.objects.filter(season=next_season, number=1).first()
    if (models.Episode.objects.filter(season=seasons_obj, number=(number - 1)).exists()):
        previous_episode = models.Episode.objects.filter(season=seasons_obj, number=(number - 1)).first()
    if not previous_episode:
        if models.Season.objects.filter(serie=serie_obj, number=season - 1).exists(): 
            prev_season =models.Season.objects.filter(serie=serie_obj, number=season - 1).first()
            previous_episode = models.Episode.objects.filter(season=prev_season).last()
    vars = {
        'seasons':seasons_obj,
        'episode':episode,
        'next_episode':next_episode,
        'previous_episode':previous_episode,
    }
    return render(request, 'base/watch.html', vars)
