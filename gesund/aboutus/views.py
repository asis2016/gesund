from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .models import ContactUs


class AboutTemplateView(LoginRequiredMixin, TemplateView):
    """ About templateview. """
    template_name = 'about/index.html'


class ContactUsCreateView(LoginRequiredMixin, CreateView):
    """ Create contactus. """
    model = ContactUs
    template_name = 'contactus/add.html'
    fields = ('subject', 'message')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
