from django.urls import path
from .views import CalorieIntakeCreateView, CaloriesIntakeDatestampListView, \
    CaloriesIntakeDatestampCollectionListView, CaloriesIntakeDeleteView, CalorieIntakeUpdateView

urlpatterns = [
    path('add/', CalorieIntakeCreateView.as_view(), name='add-calorie-intake'),
    path('<int:pk>/update/', CalorieIntakeUpdateView.as_view(), name='update-calorie-intake'),
    path('<int:pk>/delete/', CaloriesIntakeDeleteView.as_view(), name='delete-calorie-intake'),
    path('calorie-intake-datestamp-collection/<str:datestamp>/',
         CaloriesIntakeDatestampCollectionListView.as_view(), name='calorie-intake-datestamp-collection-index'),
    path('', CaloriesIntakeDatestampListView.as_view(), name='calorie-intake-datestamp-index'),
]
