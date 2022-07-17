from django.shortcuts import redirect
from django.views.generic import TemplateView
from pomodoros.models import Pomodoro


class PomodoroDetailView(TemplateView):
    """ Detailview of pomodoro."""
    model = Pomodoro
    # context_object_name = 'pomodoro_obj'
    template_name = 'pomodoros/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['id'] = self.kwargs['id']
        context['pomodoro_obj'] = Pomodoro.objects.get(pk=context['id'])

        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            id = request.POST['id']
            datestamp = request.POST['datestamp']
            Pomodoro.objects.filter(pk=id).delete()
            return redirect('pomodoro-datestamp-collection', datestamp)
