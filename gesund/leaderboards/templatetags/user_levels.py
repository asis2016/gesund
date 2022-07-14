from django import template

register = template.Library()


def level(xp):
    """
        level templatetags for leaderboards templates.
        Where, 1 level equals 1000 XP.
    """
    _xp = int(xp / 1000)
    return _xp


register.filter('level', level)
