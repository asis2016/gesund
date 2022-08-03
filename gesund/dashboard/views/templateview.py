from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from utils import get_bmi, get_bmi_interpretation

from .calorie_intake import get_calorie_intake
from .daily_goals import get_daily_goals
from .goals_reminder import GoalsReminder
from .pomodoro import get_pomodoro_list
from .quick_stats import get_quick_stats
from .steps import get_steps_list
from .water_intake import get_water_intake
from .water_intake import get_last_progress
from .weights import get_weight_list


class DashboardTemplateview(LoginRequiredMixin, TemplateView):
    """ Dashboard templateview. """
    template_name = 'dashboard/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardTemplateview, self).get_context_data(*args, **kwargs)
        context['quick_stats'] = get_quick_stats(self.request.user)
        context['calories_list'] = get_calorie_intake(self.request.user)
        context['steps_list'] = get_steps_list(self.request.user)
        context['water_intake_list'] = get_water_intake(self.request.user)
        context['water_intake_last_progress'] = get_last_progress(self.request.user)


        bmi = get_bmi(self.request.user)
        context['bmi'] = bmi
        context['bmi_interpretation'] = get_bmi_interpretation(bmi)
        context['weight_list'] = get_weight_list(self.request.user)

        context['daily_goals'] = get_daily_goals(self.request.user)
        context['pomodoro_list'] = get_pomodoro_list(self.request.user)

        # Goals
        reminder = GoalsReminder(self.request.user)
        context['goals_reminder_alert'] = reminder.get_goals_reminder()
        context['profile_reminder_alert'] = reminder.get_profile_reminder()

        return context
