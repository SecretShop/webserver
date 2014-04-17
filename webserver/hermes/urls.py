from django.conf.urls import patterns, url

from .views import GameStatsView
from .api import GamesListAPI

urlpatterns = patterns(
    '',
    url(r'^api/competition/(?P<team_pk>\d+)/games/$',
        GamesListAPI.as_view(),
        name='game_stats'),

    url(r'^competition/(?P<comp_slug>[\w-]+)/gamestats/$',
        GameStatsView.as_view(),
        name='game_stats'),
)
