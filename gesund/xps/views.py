from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from xps.models import XP


class XPsListView(LoginRequiredMixin, ListView):
    """ XPs ListView. """
    template_name = 'xps/index.html'
    model = XP
    context_object_name = 'xp_list'

    def get_queryset(self):
        usr = self.request.user.id
        return XP.objects.raw('''SELECT id, datestamp, sum(xp) as xp 
                FROM xps_xp  
                WHERE author_id = %s GROUP BY datestamp ORDER BY datestamp DESC''', [usr])

    def get_context_data(self, *args, **kwargs):
        context = super(XPsListView, self).get_context_data(*args, **kwargs)
        return context
