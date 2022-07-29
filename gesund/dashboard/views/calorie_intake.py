import sys
from calories.models import CalorieIntake
from django.db.models import Sum


def get_calorie_intake(author):
    """ Returns calories intake by a user. """
    if CalorieIntake.objects.filter(author=author):
        calories_list = CalorieIntake.objects.filter(author=author).values(
            'datestamp').annotate(total_calories=Sum('calories')).order_by('-datestamp')[:7]

        return calories_list


if __name__ == '__main__':
    get_calorie_intake(sys.argv)
