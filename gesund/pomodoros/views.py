#
#
#   This django app is not completed.

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Pomodoro


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


class PomodoroCreateView(CreateView):
    """Create pomodoro."""
    model = Pomodoro
    template_name = 'pomodoros/add.html'
    fields = ('datestamp', 'pomodoro_minutes', 'break_minutes', 'remarks')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PomodoroUpdateView(UpdateView):
    """ Update pomodoro. """
    model = Pomodoro
    context_object_name = 'pomodoro_obj'
    template_name = 'pomodoros/update.html'
    fields = ('datestamp', 'pomodoro_minutes', 'break_minutes', 'remarks')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PomodoroDeleteView(DeleteView):
    """Delete pomodoro."""
    model = Pomodoro
    context_object_name = 'pomodoro_obj'
    template_name = 'pomodoros/delete.html'
    success_url = reverse_lazy('pomodoros-index')
