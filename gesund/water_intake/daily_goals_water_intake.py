from goals.models import Goals
from utils import progress_level_percentage
from water_intake.models import WaterIntake


def get_daily_goals_water_intake(author):
    """ Returns daily goals of a user. """
    daily_goals = []
    goals = Goals.objects.filter(author=author).last()

    water_obj = WaterIntake.objects.filter(author=author).last()
    if water_obj is not None:
        goal_reach = round((water_obj.drink_progress / goals.water) * 100, 2)
        p = progress_level_percentage(goal_reach)
        daily_goals.append([goal_reach, p, 'Water intake'])

    return daily_goals


if __name__ == '__main__':
    get_daily_goals_water_intake(sys.argv)
