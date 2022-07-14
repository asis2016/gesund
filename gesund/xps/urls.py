from django.urls import path
from .views import XPsTemplateView

urlpatterns = [
    path('', XPsTemplateView.as_view(), name='xps-index')
]
