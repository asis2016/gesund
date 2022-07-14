from django.urls import path
from .views import WaterListView, WaterIntakeCreateView, WaterIntakeDeleteView, WaterIntakeUpdateView

urlpatterns = [
    path('add/', WaterIntakeCreateView.as_view(), name='add-water-progress'),
    path('<int:pk>/update/', WaterIntakeUpdateView.as_view(), name='update-water-progress'),
    path('<int:pk>/delete/', WaterIntakeDeleteView.as_view(), name='delete-water-progress'),
    path('', WaterListView.as_view(), name='water-index'),
]
