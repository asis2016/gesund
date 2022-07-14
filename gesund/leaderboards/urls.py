from django.urls import path
from .views import LeaderboardsTemplateView

urlpatterns = [
    path('', LeaderboardsTemplateView.as_view(), name='leaderboards-index')
]
