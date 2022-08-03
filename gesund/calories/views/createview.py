from calories.models import CalorieIntake
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView


class CalorieIntakeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """ Create calorie intake. """
    model = CalorieIntake
    template_name = 'calories/add.html'
    success_message = '<p class="mb-0">Food intake successfully.</p>' \
                      '<p class="mb-0">1 XP rewarded!</p>'

    def get_success_message(self, cleaned_data):
        return messages.success(self.request, self.success_message, extra_tags='bg-success')

    fields = ('datestamp', 'food', 'consume', 'calories', 'protein', 'fat', 'carb', 'sugar', 'fiber', 'food_detail_ref',
              'description')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(CalorieIntakeCreateView, self).get_context_data(*args, **kwargs)
        context['REST_API_URL'] = settings.REST_API_URL
        return context
