import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from utils import DID_YOU_KNOW
from .daily_goals_food_intake import get_daily_goals_food_intake
from goals.models import Goals
from calories.models import CalorieIntake


class CaloriesIntakeDatestampListView(LoginRequiredMixin, ListView):
    """ Get total calories intake ordered by date. """
    context_object_name = 'calories_list'
    model = CalorieIntake
    paginate_by = 10
    template_name = 'calories/index.html'

    def get_queryset(self):
        usr = self.request.user.id
        return CalorieIntake.objects.raw('''SELECT id, datestamp, sum(calories) as calories 
                FROM calories_calorieintake  
                WHERE author_id = %s GROUP BY datestamp ORDER BY datestamp DESC''', [usr])

    def get_context_data(self, *args, **kwargs):
        context = super(CaloriesIntakeDatestampListView, self).get_context_data(*args, **kwargs)
        context['did_you_know'] = random.choice(DID_YOU_KNOW['food'])
        context['daily_goals_food_intake'] = get_daily_goals_food_intake(self.request.user)
        context['goals_object_calories'] = Goals.objects.all().filter(author=self.request.user).last().calories
        return context
