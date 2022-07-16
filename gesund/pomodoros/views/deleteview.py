from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from pomodoros.models import Pomodoro


class PomodoroDeleteView(DeleteView):
    """Delete pomodoro."""
    model = Pomodoro
    context_object_name = 'pomodoro_obj'
    template_name = 'pomodoros/delete.html'
    success_url = reverse_lazy('pomodoro-index')
