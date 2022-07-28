from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from calories.models import CalorieIntake


class CaloriesIntakeDeleteView(DeleteView):
    """ Delete calories intake. """
    model = CalorieIntake
    context_object_name = 'calories_intake_obj'
    template_name = 'calories/delete.html'
    success_url = reverse_lazy('calorie-intake-datestamp-index')
