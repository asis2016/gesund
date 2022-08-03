from goals.models import Goals
from utils import progress_level_percentage
from water_intake.models import WaterIntake


def get_water_intake(author):
    """ For dashboard/water.html """
    daily_water_intake = []

    if WaterIntake.objects.all().filter(author=author):
        goals = Goals.objects.filter(author=author).last()
        water = list(WaterIntake.objects.all().filter(author=author).order_by('-datestamp')[:7])

        for i in water:
            goal_reach = round((i.drink_progress / goals.water * 100), 2)
            p = progress_level_percentage(goal_reach)
            daily_water_intake.append([i.datestamp, i.drink_progress, goal_reach, p])

    return daily_water_intake


def get_last_progress(author):
    """ Get last drinking progress for drawBottle(). """
    last_progress = []

    if WaterIntake.objects.all().filter(author=author):
        goal = Goals.objects.filter(author=author).last().water
        last_drink = WaterIntake.objects.filter(author=author).last().drink_progress
        last_progress.append([goal, last_drink])

    return last_progress


if __name__ == '__main__':
    get_water_intake(sys.argv)
    get_last_progress(sys.argv)
