from django.urls import path
from .views import add_challenge, ChallengeIndex, ChallengeUpdate, ChallengesListView

urlpatterns = [
    path('add/', add_challenge, name='add-challenge'),
    path('<int:pk>/update/', ChallengeUpdate, name='update-challenge'),
    path('', ChallengeIndex, name='challenges-index'),
]
