from calories.models import CalorieIntake
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import TemplateView
from goals.models import Goals
from pomodoros.models import Pomodoro
from profiles.models import Profile
from steps.models import Steps
from utils import get_bmi, get_bmi_interpretation, progress_level_percentage
from water_intake.models import WaterIntake
from weights.models import Weight


def quick_stats(author):
    avg_calories = CalorieIntake.objects.all().filter(author=author).aggregate(Avg('calories'))
    avg_pomodoro = Pomodoro.objects.all().filter(author=author).aggregate(Avg('pomodoro'))
    avg_steps = avg = Steps.objects.all().filter(author=author).aggregate(Avg('step_count'))
    avg_water_intake = WaterIntake.objects.all().filter(author=author).aggregate(Avg('drink_progress'))

    print(avg_water_intake)
    avg = [
        {
            'icon': 'calories.png',
            'average': round(avg_calories['calories__avg'], 2),
            'description': 'Avg. calories taken.',
            'unit': 'kcal'
        },
        {
            'icon': 'stopwatch.png',
            'average': round(avg_pomodoro['pomodoro__avg'], 2),
            'description': 'Avg. pomodoro taken.',
            'unit': 'pomodoro'
        },
        {
            'icon': 'steps.png',
            'average': round(avg_steps['step_count__avg'], 2),
            'description': 'Avg. steps taken.',
            'unit': 'steps'
        },
        {
            'icon': 'water.png',
            'average': round(avg_water_intake['drink_progress__avg'], 2),
            'description': 'Avg. drink progress.',
            'unit': 'L'
        }
    ]
    return avg


class DashboardTemplateview(LoginRequiredMixin, TemplateView):
    """Dashboard main page."""
    template_name = 'dashboard/index.html'

    def goals_reminder(self):
        """ Reminder alert! """
        goals = Goals.objects.filter(author=self.request.user).last()
        if (goals.calories and goals.water and goals.steps and goals.weight) >= 1:
            reminder_alert = 'no'
        else:
            reminder_alert = 'yes'
        return reminder_alert

    def profile_reminder(self):
        """ Profile update reminder. """
        profile = Profile.objects.filter(author=self.request.user).last()
        if profile.name:
            reminder_alert = 'no'
        else:
            reminder_alert = 'yes'
        return reminder_alert

    def goals_daily(self):
        daily_goals = []
        goals = Goals.objects.filter(author=self.request.user).last()

        # Calories
        if CalorieIntake.objects.filter(author=self.request.user):
            calories_obj = CalorieIntake.objects.filter(author=self.request.user).values('datestamp').annotate(
                total_calories=Sum('calories')).order_by('-datestamp')[:1]
            calories_obj_list = list(calories_obj)
            goal_reach = round((calories_obj_list[0]['total_calories'] / goals.calories) * 100, 2)
            p = progress_level_percentage(goal_reach)
            daily_goals.append([goal_reach, p, 'Calories'])

        # Steps
        steps_obj = Steps.objects.filter(author=self.request.user).last()
        if steps_obj is not None:
            goal_reach = round((steps_obj.step_count / goals.steps) * 100, 2)
            p = progress_level_percentage(goal_reach)
            daily_goals.append([goal_reach, p, 'Steps'])

        # Water intake
        water_obj = WaterIntake.objects.filter(author=self.request.user).last()
        if water_obj is not None:
            goal_reach = round((water_obj.drink_progress / goals.water) * 100, 2)
            p = progress_level_percentage(goal_reach)
            daily_goals.append([goal_reach, p, 'Water intake'])
        else:
            print(0)
        return daily_goals

    def water_intake_daily_progress(self):
        """ For dashboard/water.html """
        daily_goals = []

        if WaterIntake.objects.all().filter(author=self.request.user):
            goals = Goals.objects.filter(author=self.request.user).last()
            water = list(WaterIntake.objects.all().filter(author=self.request.user).order_by('-datestamp')[:7])

            for i in water:
                goal_reach = round((i.drink_progress / goals.water * 100), 2)
                p = progress_level_percentage(goal_reach)
                daily_goals.append([i.datestamp, i.drink_progress, goal_reach, p])

        return daily_goals

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardTemplateview, self).get_context_data(*args, **kwargs)

        context['quick_stats'] = quick_stats(self.request.user)

        # Calories intake
        if CalorieIntake.objects.filter(author=self.request.user):
            context['calories_list'] = CalorieIntake.objects.filter(author=self.request.user).values(
                'datestamp').annotate(total_calories=Sum('calories')).order_by('-datestamp')[:7]

        # Steps
        context['steps_list'] = Steps.objects.all().filter(author=self.request.user).order_by('-datestamp')[:7]

        # Water intake
        context['water_intake_list'] = self.water_intake_daily_progress()

        # BMI
        bmi = get_bmi(self.request.user)
        context['bmi'] = bmi
        context['bmi_interpretation'] = get_bmi_interpretation(bmi)

        # Weight
        context['weight_list'] = Weight.objects.all().filter(author=self.request.user).order_by('-datestamp')[:5]

        # Goals
        context['goals_reminder_alert'] = self.goals_reminder()
        context['profile_reminder_alert'] = self.profile_reminder()
        context['goals_daily'] = self.goals_daily()

        # Chart > not for v1
        context['pomodoro_list_chart'] = Pomodoro.objects.all().filter(author=self.request.user).order_by(
            'datestamp')[:7]

        return context


def error_404(request, exception):
    data = {}
    return render(request, 'errors/404.html', status=404)


def error_500(request, *args, **argv):
    data = {}
    return render(request, 'errors/500.html', status=500)
