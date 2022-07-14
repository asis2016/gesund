from django.urls import path

from .views import ProfileTemplateView, ProfileUpdateView, export_my_data

urlpatterns = [
    path('export-my-data', export_my_data, name='export-my-data'),
    path('<int:pk>/update/', ProfileUpdateView.as_view(), name='update-profile'),
    path('', ProfileTemplateView.as_view(), name='profile-index')
]
