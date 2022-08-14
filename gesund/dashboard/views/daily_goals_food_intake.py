from calories.models import CalorieIntake
from django.db.models import Sum
from goals.models import Goals
from utils import progress_level_percentage


def get_daily_goals_food_intake(author):
    """ Returns daily goals of a user. """
    daily_goals = []
    goals = Goals.objects.filter(author=author).last()

    if CalorieIntake.objects.filter(author=author):
        calories_obj = CalorieIntake.objects.filter(author=author).values('datestamp').annotate(
            total_calories=Sum('calories')).order_by('-datestamp')[:1]
        calories_obj_list = list(calories_obj)
        goal_reach = round((calories_obj_list[0]['total_calories'] / goals.calories) * 100, 2)
        p = progress_level_percentage(goal_reach)
        daily_goals.append([goal_reach, p, 'Pomodoro'])

    return daily_goals


if __name__ == '__main__':
    get_daily_goals_food_intake(sys.argv)
