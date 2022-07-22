from django.urls import path

from .views import ProfileTemplateView, ProfileUpdateView

urlpatterns = [
    path('<int:pk>/update/', ProfileUpdateView.as_view(), name='update-profile'),
    path('', ProfileTemplateView.as_view(), name='profile-index')
]
