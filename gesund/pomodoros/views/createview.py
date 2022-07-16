from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class PomodoroCreateTemplateView(LoginRequiredMixin, TemplateView):
    """Create pomodoro TemplateView."""
    template_name = 'pomodoros/add.html'

    # Get user specific bearer token.
    # userpass = request.user + ':' + 'H3ll_Wo22_1'
    # encoded_u = base64.b64encode(userpass.encode()).decode()

    def get_context_data(self, **kwargs):
        context = super(PomodoroCreateTemplateView, self).get_context_data(**kwargs)

        context['REST_API_URL'] = settings.REST_API_URL
        context['TOKEN'] = settings.REST_API_BEARER_TOKEN
        context['UID'] = self.request.user.id

        return context

# class PomodoroCreateView(CreateView):
#     """Create pomodoro."""
#     model = Pomodoro
#     template_name = 'pomodoros/add.html'
#     fields = ('datestamp', 'pomodoro_minutes', 'break_minutes', 'remarks')
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
