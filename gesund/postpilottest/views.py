from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from .models import PostPilotTest


class PostPilotTestCreateView(LoginRequiredMixin, CreateView):
    """ Create post pilot test. """
    model = PostPilotTest
    template_name = 'postpilottest/add.html'
    fields = '__all__'

    def form_valid(self, form):
        return super().form_valid(form)
