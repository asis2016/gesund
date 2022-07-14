from datetime import date
from profiles.models import Profile


def get_age(user):
    """ Get age util. """
    dob_obj = Profile.objects.filter(author=user).last()
    if dob_obj.dob:
        today = date.today()
        age = int((today - dob_obj.dob).days / 365.25)
    else:
        age = 'Unset'
    return age
