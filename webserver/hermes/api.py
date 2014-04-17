from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework import status

from django.shortcuts import get_object_or_404

from competition.models import Team
from greta.models import Repository

from .serializers import GameSerializer


class OnTeamOrStaff(BasePermission):
    """Permission check for users on a team or if they are staff

    Requires a "comp_slug" keyword argument in the URL
    """

    def has_permission(self, request, view):
        user = request.user
        if user.is_staff:
            return True

        pk = view.kwargs['team_pk']
        return Team.objects.filter(pk=pk, members=user).exists()


class GamesListAPI(ListAPIView):
    """List games fetched by the arena

    """

    serializer_class = GameSerializer
    paginate_by = 50
    permission_classes = (
        IsAuthenticated,
        OnTeamOrStaff,
    )

    def get_queryset(self):
        team = get_object_or_404(Team, pk=self.kwargs['team_pk'])
        return team.game_set.all()
