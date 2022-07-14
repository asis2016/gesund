from django.urls import path
from .views import HistoryTemplateView

urlpatterns = [
    path('', HistoryTemplateView.as_view(), name='history-index'),
]
