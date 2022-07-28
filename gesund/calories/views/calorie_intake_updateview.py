from django.conf import settings
from django.views.generic.edit import UpdateView

from calories.models import CalorieIntake


class CalorieIntakeUpdateView(UpdateView):
    """ Update calories intake. """
    model = CalorieIntake
    context_object_name = 'calories_obj'
    template_name = 'calories/update.html'
    fields = ('datestamp', 'food', 'consume', 'calories', 'protein', 'fat', 'carb', 'sugar', 'fiber', 'food_detail_ref',
              'description')

    def get_context_data(self, *args, **kwargs):
        context = super(CalorieIntakeUpdateView, self).get_context_data(*args, **kwargs)
        context['REST_API_URL'] = settings.REST_API_URL
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
