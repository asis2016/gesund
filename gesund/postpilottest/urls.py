from django.urls import path

from .views import PostPilotTestCreateView

urlpatterns = [
    path('', PostPilotTestCreateView.as_view(), name='post-pilot-test-questionnaire'),
]
