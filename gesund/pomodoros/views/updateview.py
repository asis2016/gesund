from django.views.generic.edit import UpdateView

from pomodoros.models import Pomodoro


class PomodoroUpdateView(UpdateView):
    """ Update pomodoro. """
    model = Pomodoro
    context_object_name = 'pomodoro_obj'
    template_name = 'pomodoros/update.html'
    fields = ('datestamp', 'short_break', 'long_break', 'remarks')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
