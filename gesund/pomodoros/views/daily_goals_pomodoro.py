from django.db.models import Sum
from goals.models import Goals
from pomodoros.models import Pomodoro
from utils import progress_level_percentage


def get_daily_goals_pomodoro(author):
    """ Returns pomodoro daily goals of a user. """
    daily_goals = []
    goals = Goals.objects.filter(author=author).last()

    if Pomodoro.objects.filter(author=author):
        pomodoro_obj = Pomodoro.objects.filter(author=author).values('datestamp').annotate(
            total_pomodoro=Sum('pomodoro')).order_by('-datestamp')[:1]
        pomodoro_obj_list = list(pomodoro_obj)
        goal_reach = round((pomodoro_obj_list[0]['total_pomodoro'] / goals.pomodoro) * 100, 2)
        p = progress_level_percentage(goal_reach)
        daily_goals.append([goal_reach, p, 'Pomodoro'])

    return daily_goals


if __name__ == '__main__':
    get_daily_goals_Pomodoro(sys.argv)
