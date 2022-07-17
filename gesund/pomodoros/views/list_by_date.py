from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from pomodoros.models import Pomodoro


class PomodoroListViewByDate(LoginRequiredMixin, ListView):
    """ List all pomodoros by datestamp. """
    context_object_name = 'pomodoro_list'
    model = Pomodoro
    template_name = 'pomodoros/list_by_date.html'

    def get_queryset(self):
        datestamp = self.kwargs['datestamp']
        usr = self.request.user.id
        return Pomodoro.objects.raw('''SELECT * FROM pomodoros_pomodoro 
        WHERE author_id = %s AND datestamp = %s ORDER BY datestamp DESC''', [usr, datestamp])

    def get_context_data(self, *args, **kwargs):
        context = super(PomodoroListViewByDate, self).get_context_data(*args, **kwargs)
        context['datestamp'] = self.kwargs['datestamp']
        return context
