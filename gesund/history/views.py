from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import History


class HistoryTemplateView(LoginRequiredMixin, TemplateView):
    """ History/Timeline templateview. """
    template_name = 'history/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HistoryTemplateView, self).get_context_data(*args, **kwargs)
        context['history_list'] = History.objects.all().filter(author=self.request.user).order_by('-datestamp')
        return context
