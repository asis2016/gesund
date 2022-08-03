from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from pomodoros.models import Pomodoro


class PomodoroDetailView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """ Detailview of pomodoro."""
    model = Pomodoro
    context_object_name = 'pomodoro_obj'
    template_name = 'pomodoros/detail.html'

    def get_success_message(self, cleaned_data):
        return messages.success(self.request, 'Pomodoro record deleted.', extra_tags='bg-danger')

    def get_success_url(self):
        datestamp = self.object.datestamp
        return reverse_lazy('pomodoro-datestamp-collection', kwargs={'datestamp': datestamp})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['id'] = self.kwargs['id']
    #     context['pomodoro_obj'] = Pomodoro.objects.get(pk=context['id'])
    #
    #     return context

    # def post(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         id = request.POST['id']
    #         datestamp = request.POST['datestamp']
    #         Pomodoro.objects.filter(pk=id).delete()
    #         return redirect('pomodoro-datestamp-collection', datestamp)
