from goals.models import Goals
from profiles.models import Profile


class GoalsReminder:
    """ Goals reminder. """

    def __init__(self, author):
        self.author = author

    def get_goals_reminder(self):
        """ Reminder alert! """
        goals = Goals.objects.filter(author=self.author).last()
        return 'no' if (goals.calories and goals.water and goals.steps and goals.weight) >= 1 else 'yes'

    def get_profile_reminder(self):
        """ Profile update reminder. """
        profile = Profile.objects.filter(author=self.author).last()
        return 'no' if profile.name else 'yes'
