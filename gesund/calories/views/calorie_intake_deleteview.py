from calories.models import CalorieIntake
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


class CaloriesIntakeDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """ Delete calories intake. """
    model = CalorieIntake
    context_object_name = 'calories_intake_obj'
    template_name = 'calories/delete.html'
    # success_message = 'Delete!'
    success_url = reverse_lazy('calorie-intake-datestamp-index')
