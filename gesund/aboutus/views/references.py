from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class ReferencesTemplateView(LoginRequiredMixin, TemplateView):
    """ References templateview. """
    template_name = 'references/index.html'
