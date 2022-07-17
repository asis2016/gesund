from django.urls import path

from .views import AboutTemplateView, ContactUsCreateView

urlpatterns = [
    path('contact-us/', ContactUsCreateView.as_view(), name='contact-us'),
    path('', AboutTemplateView.as_view(), name='about'),
]
