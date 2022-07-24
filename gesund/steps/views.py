import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Steps

did_you_know = [
    ['title 1', 'content 1'],
    ['title 2', 'content 2'],
    ['title 3', 'content 3'],
    ['title 4', 'content 4'],
    ['title 5', 'content 5']
]


class StepsListView(LoginRequiredMixin, ListView):
    """ Steps listview. """
    context_object_name = 'steps_list'
    model = Steps
    paginate_by = 10
    template_name = 'steps/index.html'

    def get_queryset(self):
        return Steps.objects.filter(author=self.request.user).order_by('-datestamp')

    def get_context_data(self, **kwargs):
        context = super(StepsListView, self).get_context_data(**kwargs)
        context['steps_list_chart'] = Steps.objects.all().filter(author=self.request.user).order_by(
            'datestamp')

        context['did_you_know'] = random.choice(did_you_know)

        return context


class StepsCreateView(LoginRequiredMixin, CreateView):
    """ Create steps. """
    model = Steps
    template_name = 'steps/add.html'
    fields = ('datestamp', 'step_count')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StepsUpdateView(LoginRequiredMixin, UpdateView):
    """ Update steps. """
    model = Steps
    context_object_name = 'steps_obj'
    template_name = 'steps/update.html'
    fields = ('datestamp', 'step_count')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StepsDeleteView(LoginRequiredMixin, DeleteView):
    """ Delete steps. """
    model = Steps
    context_object_name = 'steps_obj'
    template_name = 'steps/delete.html'
    success_url = reverse_lazy('steps-index')
