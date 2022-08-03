from calories.models import CalorieIntake
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView


class CalorieIntakeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """ Update calories intake. """
    model = CalorieIntake
    context_object_name = 'calories_obj'
    template_name = 'calories/update.html'
    fields = ('datestamp', 'food', 'consume', 'calories', 'protein', 'fat', 'carb', 'sugar', 'fiber', 'food_detail_ref',
              'description')

    def get_success_message(self, cleaned_data):
        return messages.success(self.request, 'Food intake updated successfully.', extra_tags='bg-warning')

    def get_context_data(self, *args, **kwargs):
        context = super(CalorieIntakeUpdateView, self).get_context_data(*args, **kwargs)
        context['REST_API_URL'] = settings.REST_API_URL
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
