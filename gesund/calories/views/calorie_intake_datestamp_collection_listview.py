from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from calories.models import CalorieIntake


class CaloriesIntakeDatestampCollectionListView(LoginRequiredMixin, ListView):
    """ Get calories intake on datestamp by food ASC. """
    context_object_name = 'calories_list'
    model = CalorieIntake
    paginate_by = 2
    template_name = 'calories/index_datestamp_collection.html'

    def get_queryset(self):
        datestamp = self.kwargs['datestamp']
        usr = self.request.user.id
        return CalorieIntake.objects.raw('''SELECT * FROM calories_calorieintake 
        WHERE author_id = %s AND datestamp = %s ORDER BY food ASC''', [usr, datestamp])

    def get_context_data(self, *args, **kwargs):
        context = super(CaloriesIntakeDatestampCollectionListView, self).get_context_data(*args, **kwargs)
        context['datestamp'] = self.kwargs['datestamp']
        return context
