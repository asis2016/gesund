from django.urls import path

from .views import PomodoroDetailView, PomodoroListView, PomodoroCreateTemplateView, PomodoroListViewByDate

urlpatterns = [
    path('add/', PomodoroCreateTemplateView.as_view(), name='add-pomodoro'),
    path('<int:pk>/detail/', PomodoroDetailView.as_view(), name='detail-pomodoro'),
    path('pomodoro-datestamp-collection/<str:datestamp>/', PomodoroListViewByDate.as_view(),
         name='pomodoro-datestamp-collection'),
    path('', PomodoroListView.as_view(), name='pomodoro-index'),
]
