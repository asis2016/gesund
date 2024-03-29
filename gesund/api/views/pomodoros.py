from api.serializers import PomodoroSerializer
from pomodoros.models import Pomodoro
from rest_framework import permissions

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class PomodoroListCreateAPIView(ListCreateAPIView):
    """ Lists or Create pomodoro(s). """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Pomodoro.objects.all()
    serializer_class = PomodoroSerializer


class PomodoroRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or destroy pomodoro(s). """
    queryset = Pomodoro.objects.all()
    serializer_class = PomodoroSerializer
