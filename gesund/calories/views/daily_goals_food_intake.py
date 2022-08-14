from django.db.models import Sum
from goals.models import Goals
from pomodoros.models import Pomodoro
from utils import progress_level_percentage
from calories.models import CalorieIntake


def get_daily_goals_food_intake(author):
    """ Returns daily food intake progress. """
    daily_goals = []
    goals = Goals.objects.filter(author=author).last()

    if CalorieIntake.objects.filter(author=author):
        calorie_intake_obj = CalorieIntake.objects.filter(author=author).values('datestamp').annotate(
            total_calories=Sum('calories')).order_by('-datestamp')[:1]
        calorie_intake_obj_list = list(calorie_intake_obj)
        goal_reach = round((calorie_intake_obj_list[0]['total_calories'] / goals.calories) * 100, 2)
        p = progress_level_percentage(goal_reach)
        daily_goals.append([goal_reach, p, 'Calories'])

    return daily_goals


if __name__ == '__main__':
    get_daily_goals_food_intake(sys.argv)
