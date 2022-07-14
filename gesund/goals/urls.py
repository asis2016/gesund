from django.urls import path
from .views import GoalsTemplateView, GoalsUpdateView

urlpatterns = [
    path('<int:pk>/update', GoalsUpdateView.as_view(), name='update-goals'),
    path('', GoalsTemplateView.as_view(), name='goals-index'),
]
