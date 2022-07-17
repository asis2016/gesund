from django.urls import path

from .views import PomodoroListView, PomodoroCreateTemplateView, PomodoroDeleteView, PomodoroListViewByDate

urlpatterns = [
    path('add/', PomodoroCreateTemplateView.as_view(), name='add-pomodoro'),
    # update not required.
    # path('<int:pk>/update/', PomodoroUpdateView.as_view(), name='update-pomodoro'),
    path('<int:pk>/delete/', PomodoroDeleteView.as_view(), name='delete-pomodoro'),
    path('pomodoro-datestamp-collection/<str:datestamp>', PomodoroListViewByDate.as_view(),
         name='pomodoro-datestamp-collection'),
    path('', PomodoroListView.as_view(), name='pomodoro-index'),
]
