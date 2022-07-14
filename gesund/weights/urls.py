from django.urls import path
from .views import WeightCreateView, WeightDeleteView, WeightUpdateView, WeightListView

urlpatterns = [
    path('add/', WeightCreateView.as_view(), name='add-weight'),
    path('<int:pk>/delete/', WeightDeleteView.as_view(), name='delete-weight'),
    path('<int:pk>/update/', WeightUpdateView.as_view(), name='update-weight'),
    path('', WeightListView.as_view(), name='weight-index'),
]
