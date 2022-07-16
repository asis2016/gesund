from api.serializers import PomodoroSerializer
from pomodoros.models import Pomodoro
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView


class PomodoroListCreateAPIView(ListCreateAPIView):
    """ Lists or Create pomodoro(s). """
    queryset = Pomodoro.objects.all()
    serializer_class = PomodoroSerializer


class PomodoroListAPIView(ListAPIView):
    """ Lists all pomodoro taken. """
    serializer_class = PomodoroSerializer

    def get_queryset(self):
        return Pomodoro.objects.all()


class PomodoroRetrieveAPIView(RetrieveAPIView):
    """ Retrieve pomodoro by id. """
    serializer_class = PomodoroSerializer

    def get_queryset(self):
        return Pomodoro.objects.all().filter(author=self.request.user)
