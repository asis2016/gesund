from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from goals.models import Goals

from .models import Weight


class WeightListView(LoginRequiredMixin, ListView):
    """ Weight listview and filtered by the requested user. """
    context_object_name = 'weight_list'
    model = Weight
    paginate_by = 10
    template_name = 'weights/index.html'

    def get_queryset(self):
        return Weight.objects.all().filter(author=self.request.user).order_by('-datestamp')

    def get_context_data(self, **kwargs):
        context = super(WeightListView, self).get_context_data(**kwargs)
        context['weight_list_chart'] = Weight.objects.all().filter(author=self.request.user).order_by(
            'datestamp')

        context['goals_object_weight'] = Goals.objects.all().filter(author=self.request.user).last().weight

        # todo: context random messages
        context['random_message'] = {
            "title": "title",
            "msg": "message"
        }
        return context


class WeightCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """ Create weight. """
    model = Weight
    template_name = 'weights/add.html'
    fields = ('datestamp', 'weight')
    success_message = 'Weight added successfully.'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class WeightUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """ Update weight. """
    model = Weight
    context_object_name = 'weight_obj'
    template_name = 'weights/update.html'
    fields = ('datestamp', 'weight')

    def get_success_message(self, cleaned_data):
        return messages.success(self.request, 'Weight updated successfully.', extra_tags='bg-warning')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class WeightDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """ Delete weight. """
    model = Weight
    context_object_name = 'weight_obj'
    template_name = 'weights/delete.html'
    success_url = reverse_lazy('weight-index')

    def get_success_message(self, cleaned_data):
        return messages.success(self.request, 'Weight record deleted!', extra_tags='bg-danger')
