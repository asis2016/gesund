import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Steps

did_you_know = [
    {
        'img': 'steps_walking_1.png',
        'content': 'Individuals who take more than 12,500 steps per day are likely to be classified as highly active people.'
    },
    {
        'img': 'steps_walking_4.jpg',
        'content': 'Individuals should accumulate at least 30 minutes of moderate-intensity activity (i.e., brisk walking) on a daily basis - Public health recommendations endorsed by the US Surgeon General'
    },
    {
        'img': 'steps_walking_2.png',
        'content': 'People who accumulate at least 10,000 steps per day have less body fat and lower blood pressure than their less active counterparts.'
    },
    {
        'img': 'steps_walking_3.jpg',
        'content': '<ol>'
                   '<li>"Sedentary" lifestyle indicates < 5,000 steps/day.</li>'
                   '<li>"Low active" lifestyle indicates 5,000 - 7,499 steps/day.</li>'
                   '<li>"Somewhat active" lifestyle indicates 7,500 - 9,999 steps/day.</li>'
                   '<li>"Active" people are identified who take 10,000 steps/day.</li>'
                   '<li>Individual who takes more than 12,500 steps/day tend to have a "Highly active" lifestyle.</li></ol>'
    }
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


class StepsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """ Create steps. """
    model = Steps
    template_name = 'steps/add.html'
    fields = ('datestamp', 'step_count')
    success_message = 'Steps added successfully.'

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
