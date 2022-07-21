from django.db import models
from django.urls import reverse


class PostPilotTest(models.Model):
    """ PostPilotTest model (questionnaire for pilot test) """
    id = models.AutoField(primary_key=True, editable=False)
    datestamp = models.DateField()

    physical_activity_type = models.TextField(
        verbose_name='During the experiment period, what type of physical activities did you perform?'
    )
    physical_activity_level = models.TextField()
    physical_activity_active_days = models.TextField()
    physical_activity_active_hours = models.TextField()
    avg_work_week_sitting_hours = models.TextField()
    daily_work_week_sitting_hours = models.TextField()
    daily_tv_hours = models.TextField()
    daily_screen_play_hours = models.TextField()
    daily_screen_hours = models.TextField()
    bed_time = models.TextField()
    fall_asleep_in_minutes = models.TextField()
    wake_up_time = models.TextField()
    daily_sleep_hours = models.TextField()
    overall_sleep_quality = models.TextField()
    nutrition_tracker_usage = models.TextField()
    application_usage = models.TextField()
    likelihood_intervention_usage = models.TextField()
    feature_wish_list = models.TextField()
    rating = models.TextField()

    weight = models.FloatField()
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.datestamp} - {self.weight} kg'

    def get_absolute_url(self):
        return reverse('weight-index')
