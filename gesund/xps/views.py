from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from xps.models import XP


class XPsTemplateView(LoginRequiredMixin, TemplateView):
    """ XPs templateview. """
    template_name = 'xps/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(XPsTemplateView, self).get_context_data(*args, **kwargs)
        context['xp_list'] = XP.objects.filter(author=self.request.user).order_by('-datestamp')
        return context
