import sys
from steps.models import Steps


def get_steps_list(author):
    """ Returns steps from a user. """
    steps_list = Steps.objects.all().filter(author=author).order_by('-datestamp')
    return steps_list


if __name__ == '__main__':
    get_steps_list(sys.argv)
