from django.urls import path

from .views import XPsListView

urlpatterns = [
    path('', XPsListView.as_view(), name='xps-index')
]
