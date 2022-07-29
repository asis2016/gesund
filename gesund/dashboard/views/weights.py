import sys
from weights.models import Weight


def get_weight_list(author):
    """ Returns weights from a user. """
    weight_list = Weight.objects.all().filter(author=author).order_by('-datestamp')
    return weight_list


if __name__ == '__main__':
    get_weight_list(sys.argv)
