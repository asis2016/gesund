from django.db.models import Sum
from xps.models import XP


def get_total_xp(user):
    """ Get total XP. """
    if XP.objects.filter(author=user):
        total_xp = XP.objects.filter(author=user).aggregate(Sum('xp'))
    else:
        total_xp = 'Unset'
    return total_xp
