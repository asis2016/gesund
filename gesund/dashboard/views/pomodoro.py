import sys
from django.db.models import Sum
from pomodoros.models import Pomodoro


def get_pomodoro_list(author):
    """ Returns pomodoro from a user. """
    if Pomodoro.objects.filter(author=author):
        pomodoro_list = Pomodoro.objects.all().filter(author=author). \
            values('datestamp').annotate(total_pomodoro=Sum('pomodoro')).order_by('-datestamp')

        return pomodoro_list


if __name__ == '__main__':
    get_pomodoro_list(sys.argv)
