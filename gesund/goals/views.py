from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Goals


class GoalsTemplateView(LoginRequiredMixin, TemplateView):
    """ Goals templateview. """
    template_name = 'goals/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(GoalsTemplateView, self).get_context_data(*args, **kwargs)
        context['goals_list'] = Goals.objects.all().filter(author=self.request.user)
        return context


class GoalsUpdateView(LoginRequiredMixin, UpdateView):
    """ Update goals. """
    model = Goals
    context_object_name = 'goals_obj'
    template_name = 'goals/update.html'
    fields = ('calories', 'steps', 'water', 'weight',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
