from django.urls import path

from .views import SignUpView, UserSignLogTemplateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup')
]
