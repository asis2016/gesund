from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
        return context


class WeightCreateView(LoginRequiredMixin, CreateView):
    """ Create weight. """
    model = Weight
    template_name = 'weights/add.html'
    fields = ('datestamp', 'weight')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class WeightUpdateView(LoginRequiredMixin, UpdateView):
    """ Update weight. """
    model = Weight
    context_object_name = 'weight_obj'
    template_name = 'weights/update.html'
    fields = ('datestamp', 'weight')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class WeightDeleteView(LoginRequiredMixin, DeleteView):
    """ Delete weight. """
    model = Weight
    context_object_name = 'weight_obj'
    template_name = 'weights/delete.html'
    success_url = reverse_lazy('weight-index')
