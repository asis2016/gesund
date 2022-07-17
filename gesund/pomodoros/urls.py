from django.urls import path

from .views import PomodoroDetailView, PomodoroListView, PomodoroCreateTemplateView, PomodoroListViewByDate

urlpatterns = [
    path('add/', PomodoroCreateTemplateView.as_view(), name='add-pomodoro'),
    # UpdateView is obsolete
    # path('<int:pk>/update/', PomodoroUpdateView.as_view(), name='update-pomodoro'),

    # DeleteView is obsolete
    # path('<int:pk>/delete/', PomodoroDeleteView.as_view(), name='delete-pomodoro'),

    path('detail/<str:id>', PomodoroDetailView.as_view(), name='detail-pomodoro'),
    path('pomodoro-datestamp-collection/<str:datestamp>', PomodoroListViewByDate.as_view(),
         name='pomodoro-datestamp-collection'),
    path('', PomodoroListView.as_view(), name='pomodoro-index'),
]
