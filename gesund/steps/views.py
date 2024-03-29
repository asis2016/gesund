import random
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from goals.models import Goals
from utils import DID_YOU_KNOW

from .daily_goals_steps import get_daily_goals_steps
from .models import Steps


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

        # context['steps_list_chart'] = Steps.objects.all().filter(author=self.request.user).order_by('datestamp')

        context['did_you_know'] = random.choice(DID_YOU_KNOW['steps'])
        context['steps_list_chart'] = Steps.objects.all().filter(author=self.request.user).order_by('-datestamp')
        context['daily_goals_steps'] = get_daily_goals_steps(self.request.user)
        context['goals_object_steps'] = Goals.objects.all().filter(author=self.request.user).last().steps
        return context


class StepsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """ Create steps. """
    model = Steps
    template_name = 'steps/add.html'
    fields = ('datestamp', 'step_count')
    success_message = '<p class="mb-0">Steps added successfully.</p>' \
                      '<p class="mb-0">1 XP rewarded!</p>'

    def get_success_message(self, cleaned_data):
        return messages.success(self.request, self.success_message, extra_tags='bg-success')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StepsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """ Update steps. """
    model = Steps
    context_object_name = 'steps_obj'
    template_name = 'steps/update.html'
    fields = ('datestamp', 'step_count')

    def get_success_message(self, cleaned_data):
        return messages.success(self.request, 'Steps updated successfully.', extra_tags='bg-warning')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StepsDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """ Delete steps. """
    model = Steps
    context_object_name = 'steps_obj'
    template_name = 'steps/delete.html'
    success_url = reverse_lazy('steps-index')

    def get_success_message(self, cleaned_data):
        return messages.error(self.request, 'Steps record deleted!', extra_tags='bg-danger')
