from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class AboutTemplateView(LoginRequiredMixin, TemplateView):
    """ About templateview. """
    template_name = 'about/index.html'
