from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.serializers import PomodoroSerializer
from pomodoros.models import Pomodoro


class PomodoroListAPIView(ListAPIView):
    """ Lists all pomodoro taken. """
    serializer_class = PomodoroSerializer

    def get_queryset(self):
        return Pomodoro.objects.all().filter(author=self.request.user)


class PomodoroRetrieveAPIView(RetrieveAPIView):
    """ Retrieve pomodoro by id. """
    serializer_class = PomodoroSerializer

    def get_queryset(self):
        return Pomodoro.objects.all().filter(author=self.request.user)
