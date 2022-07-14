from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from xps.models import XP


class LeaderboardsTemplateView(LoginRequiredMixin, TemplateView):
    """
    - Leaderboards templateview.
    - Custom SQL query returns xp_list context.
    """
    template_name = 'leaderboards/index.html'

    query = '''SELECT auth_user.id, auth_user.username, IFNULL(sum(xps_xp.xp), 0) AS total_xp
                FROM xps_xp
                RIGHT JOIN auth_user 
                on xps_xp.author_id = auth_user.id
                GROUP BY auth_user.id
                ORDER BY total_xp DESC'''

    def get_context_data(self, *args, **kwargs):
        context = super(LeaderboardsTemplateView, self).get_context_data(*args, **kwargs)
        context['xp_list'] = XP.objects.raw(self.query)
        return context
