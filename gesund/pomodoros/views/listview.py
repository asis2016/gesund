import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from pomodoros.models import Pomodoro
from utils import DID_YOU_KNOW

from goals.models import Goals

from .daily_goals_pomodoro import get_daily_goals_pomodoro


class PomodoroListView(LoginRequiredMixin, ListView):
    """ List all pomodoro by group of datestamp ."""
    context_object_name = 'pomodoro_list'
    model = Pomodoro
    paginate_by = 10
    template_name = 'pomodoros/index.html'

    def get_queryset(self):
        usr = self.request.user.id
        return Pomodoro.objects.raw('''SELECT id, datestamp, 
                sum(pomodoro) as total_pomodoro
                FROM pomodoros_pomodoro  
                WHERE author_id = %s GROUP BY datestamp ORDER BY datestamp DESC''', [usr])

    def get_context_data(self, **kwargs):
        context = super(PomodoroListView, self).get_context_data(**kwargs)
        context['pomodoro_list_chart'] = Pomodoro.objects.all().filter(author=self.request.user).order_by(
            'datestamp')
        context['did_you_know'] = random.choice(DID_YOU_KNOW['pomodoro'])
        context['daily_goals_pomodoro'] = get_daily_goals_pomodoro(self.request.user)
        context['goals_object_pomodoro'] = Goals.objects.all().filter(author=self.request.user).last().pomodoro
        return context
