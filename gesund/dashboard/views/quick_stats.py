import sys
from calories.models import CalorieIntake
from django.db.models import Avg
from pomodoros.models import Pomodoro
from steps.models import Steps
from water_intake.models import WaterIntake


def get_quick_stats(author):
    """ Return quick stats of a user. """
    avg_calories = CalorieIntake.objects.all().filter(author=author).aggregate(Avg('calories'))['calories__avg']
    avg_pomodoros = Pomodoro.objects.all().filter(author=author).aggregate(Avg('pomodoro'))['pomodoro__avg']
    avg_steps = Steps.objects.all().filter(author=author).aggregate(Avg('step_count'))['step_count__avg']
    avg_water_intake = WaterIntake.objects.all().filter(author=author).aggregate(Avg('drink_progress'))[
        'drink_progress__avg']

    avg = [
        {
            'icon': 'calories.png',
            'average': round(avg_calories, 2) if avg_calories is not None else '0',
            'description': 'Avg. calories taken.',
            'unit': 'kcal'
        },
        {
            'icon': 'stopwatch.png',
            'average': round(avg_pomodoros, 2) if avg_pomodoros is not None else '0',
            'description': 'Avg. pomodoro taken.',
            'unit': 'pomodoro'
        },
        {
            'icon': 'steps.png',
            'average': round(avg_steps, 2) if avg_steps is not None else '0',
            'description': 'Avg. steps taken.',
            'unit': 'steps'
        },
        {
            'icon': 'water.png',
            'average': round(avg_water_intake, 2) if avg_water_intake is not None else '0',
            'description': 'Avg. drink progress.',
            'unit': 'L'
        }
    ]
    return avg


if __name__ == '__main__':
    get_quick_stats(sys.argv)
