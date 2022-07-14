from django.urls import path
from .views import StepsListView, StepsCreateView, StepsUpdateView, StepsDeleteView

urlpatterns = [
    path('add/', StepsCreateView.as_view(), name='add-steps'),
    path('<int:pk>/update/', StepsUpdateView.as_view(), name='update-steps'),
    path('<int:pk>/delete/', StepsDeleteView.as_view(), name='delete-steps'),
    path('', StepsListView.as_view(), name='steps-index'),
]
