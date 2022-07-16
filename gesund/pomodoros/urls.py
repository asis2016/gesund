#
#
#   This django app is not completed.

from django.urls import path
from .views import PomodoroListView, PomodoroCreateTemplateView, PomodoroUpdateView, PomodoroDeleteView

urlpatterns = [
    path('pomodoros/add/', PomodoroCreateTemplateView.as_view(), name='add-pomodoro'),
    path('pomodoros/<int:pk>/update/', PomodoroUpdateView.as_view(), name='update-pomodoro'),
    path('pomodoros/<int:pk>/delete/', PomodoroDeleteView.as_view(), name='delete-pomodoro'),
    path('', PomodoroListView.as_view(), name='pomodoro-index'),
]
