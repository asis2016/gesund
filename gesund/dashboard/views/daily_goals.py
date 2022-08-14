from django.db.models import Sum
from goals.models import Goals
from pomodoros.models import Pomodoro
from steps.models import Steps
from utils import progress_level_percentage
from water_intake.models import WaterIntake


def get_daily_goals(author):
    """ Returns daily goals of a user. """
    daily_goals = []
    goals = Goals.objects.filter(author=author).last()

    # Pomodoro
    if Pomodoro.objects.filter(author=author):
        pomodoro_obj = Pomodoro.objects.filter(author=author).values('datestamp').annotate(
            total_pomodoro=Sum('pomodoro')).order_by('-datestamp')[:1]
        pomodoro_obj_list = list(pomodoro_obj)
        goal_reach = round((pomodoro_obj_list[0]['total_pomodoro'] / goals.pomodoro) * 100, 2)
        p = progress_level_percentage(goal_reach)
        daily_goals.append([goal_reach, p, 'Pomodoro'])

    # Steps
    steps_obj = Steps.objects.filter(author=author).last()
    if steps_obj is not None:
        goal_reach = round((steps_obj.step_count / goals.steps) * 100, 2)
        p = progress_level_percentage(goal_reach)
        daily_goals.append([goal_reach, p, 'Steps'])

    # Water intake
    water_obj = WaterIntake.objects.filter(author=author).last()
    if water_obj is not None:
        goal_reach = round((water_obj.drink_progress / goals.water) * 100, 2)
        p = progress_level_percentage(goal_reach)
        daily_goals.append([goal_reach, p, 'Water intake'])

    return daily_goals


if __name__ == '__main__':
    get_daily_goals(sys.argv)
