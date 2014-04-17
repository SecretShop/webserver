from rest_framework import serializers
from greta.models import Repository
from competition.models import Team, Game


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('id', 'name', 'slug', 'eligible_to_win')


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
