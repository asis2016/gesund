from calories.models import CalorieIntake
from django.db.models import Sum
from goals.models import Goals
from steps.models import Steps
from utils import progress_level_percentage
from water_intake.models import WaterIntake


def get_daily_goals(author):
    """ Returns daily goals of a user. """
    daily_goals = []
    goals = Goals.objects.filter(author=author).last()

    # Calories
    if CalorieIntake.objects.filter(author=author):
        calories_obj = CalorieIntake.objects.filter(author=author).values('datestamp').annotate(
            total_calories=Sum('calories')).order_by('-datestamp')[:1]
        calories_obj_list = list(calories_obj)
        goal_reach = round((calories_obj_list[0]['total_calories'] / goals.calories) * 100, 2)
        p = progress_level_percentage(goal_reach)
        daily_goals.append([goal_reach, p, 'Calories'])

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
    else:
        print(0)
    return daily_goals


if __name__ == '__main__':
    get_daily_goals(sys.argv)
