import random
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from utils import DID_YOU_KNOW

from .daily_goals_water_intake import get_daily_goals_water_intake

from goals.models import Goals

from .models import WaterIntake


class WaterListView(LoginRequiredMixin, ListView):
    """ Water intake listview. """
    context_object_name = 'water_intake_list'
    model = WaterIntake
    paginate_by = 10
    template_name = 'water_intake/index.html'

    def get_queryset(self):
        return WaterIntake.objects.all().filter(author=self.request.user).order_by(
            '-datestamp')

    def get_context_data(self, **kwargs):
        context = super(WaterListView, self).get_context_data(**kwargs)
        context['water_intake_list_chart'] = WaterIntake.objects.all().filter(author=self.request.user).order_by(
            'datestamp')
        context['did_you_know'] = random.choice(DID_YOU_KNOW['water'])
        context['daily_goals_water_intake'] = get_daily_goals_water_intake(self.request.user)

        context['goals_object_water_intake'] = Goals.objects.all().filter(author=self.request.user).last().water
        return context


class WaterIntakeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """ Create water intake. """
    model = WaterIntake
    template_name = 'water_intake/add.html'
    fields = ('datestamp', 'drink_progress')
    success_message = '<p class="mb-0">Water intake successfully.</p>' \
                      '<p class="mb-0">1 XP rewarded!</p>'

    def get_success_message(self, cleaned_data):
        return messages.success(self.request, self.success_message, extra_tags='bg-success')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'SAVED!')
        return super().form_valid(form)


class WaterIntakeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """ Update water intake. """
    model = WaterIntake
    context_object_name = 'water_obj'
    template_name = 'water_intake/update.html'
    fields = ['datestamp', 'drink_progress']

    def get_success_message(self, cleaned_data):
        return messages.success(self.request, 'Water intake updated successfully.', extra_tags='bg-warning')

    def dispatch(self, request, *args, **kwargs):
        """ make user only this user is allowed! """
        obj = self.get_object()
        if obj.author != self.request.user:
            return redirect(obj)
        return super(WaterIntakeUpdateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class WaterIntakeDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """ Delete water intake. """
    model = WaterIntake
    context_object_name = 'water_obj'
    template_name = 'water_intake/delete.html'
    success_url = reverse_lazy('water-index')

    def get_success_message(self, cleaned_data):
        return messages.success(self.request, 'Water intake record deleted!', extra_tags='bg-danger')
