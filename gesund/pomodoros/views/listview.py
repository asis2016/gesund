from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from pomodoros.models import Pomodoro


class PomodoroListView(LoginRequiredMixin, ListView):
    """List all pomodoro."""
    context_object_name = 'pomodoro_list'
    model = Pomodoro
    paginate_by = 10
    template_name = 'pomodoros/index.html'

    def get_queryset(self):
        return Pomodoro.objects.all().filter(author=self.request.user).order_by('-datestamp')

    def get_context_data(self, **kwargs):
        context = super(PomodoroListView, self).get_context_data(**kwargs)
        context['pomodoro_list_chart'] = Pomodoro.objects.all().filter(author=self.request.user).order_by(
            'datestamp')
        return context
