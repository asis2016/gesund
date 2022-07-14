from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CalorieIntake


class CalorieIntakeCreateView(CreateView):
    """ Create calorie intake. """
    model = CalorieIntake
    template_name = 'calories/add.html'
    fields = ('datestamp', 'food', 'consume', 'calories', 'protein', 'fat', 'carb', 'sugar', 'fiber', 'food_detail_ref',
              'description')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(CalorieIntakeCreateView, self).get_context_data(*args, **kwargs)
        return context


class CaloriesIntakeDatestampListView(ListView):
    """ Get total calories intake ordered by date. """
    context_object_name = 'calories_list'
    model = CalorieIntake
    paginate_by = 10
    template_name = 'calories/index.html'

    def get_queryset(self):
        usr = self.request.user.id
        return CalorieIntake.objects.raw('''SELECT id, datestamp, sum(calories) as calories 
                FROM calories_calorieintake  
                WHERE author_id = %s GROUP BY datestamp ORDER BY datestamp DESC''', [usr])


class CaloriesIntakeDatestampCollectionListView(ListView):
    """ Get calories intake on datestamp by food ASC. """
    context_object_name = 'calories_list'
    model = CalorieIntake
    paginate_by = 1
    template_name = 'calories/index-datestamp-collection.html'

    def get_queryset(self):
        datestamp = self.kwargs['datestamp']
        usr = self.request.user.id
        return CalorieIntake.objects.raw('''SELECT * FROM calories_calorieintake 
        WHERE author_id = %s AND datestamp = %s ORDER BY food ASC''', [usr, datestamp])

    def get_context_data(self, *args, **kwargs):
        context = super(CaloriesIntakeDatestampCollectionListView, self).get_context_data(*args, **kwargs)
        context['datestamp'] = self.kwargs['datestamp']
        return context


class CalorieIntakeUpdateView(UpdateView):
    """ Update calories intake. """
    model = CalorieIntake
    context_object_name = 'calories_obj'
    template_name = 'calories/update.html'
    fields = ('datestamp', 'food', 'consume', 'calories', 'protein', 'fat', 'carb', 'sugar', 'fiber', 'food_detail_ref',
              'description')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CaloriesIntakeDeleteView(DeleteView):
    """ Delete calories intake. """
    model = CalorieIntake
    context_object_name = 'calories_intake_obj'
    template_name = 'calories/delete.html'
    success_url = reverse_lazy('calorie-intake-datestamp-index')
