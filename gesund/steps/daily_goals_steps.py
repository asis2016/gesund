from goals.models import Goals
from steps.models import Steps
from utils import progress_level_percentage


def get_daily_goals_steps(author):
    """ Returns daily goals of a user. """
    daily_goals = []
    goals = Goals.objects.filter(author=author).last()

    steps_obj = Steps.objects.filter(author=author).last()

    if steps_obj is not None:
        goal_reach = round((steps_obj.step_count / goals.steps) * 100, 2)
        p = progress_level_percentage(goal_reach)
        daily_goals.append([goal_reach, p, 'Steps'])

    return daily_goals


if __name__ == '__main__':
    get_daily_goals_steps(sys.argv)
