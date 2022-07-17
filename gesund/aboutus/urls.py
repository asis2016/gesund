from django.urls import path

from .views import AboutTemplateView, ContactUsCreateView, ContactUsSuccessTemplateView

urlpatterns = [
    path('contact-us/', ContactUsCreateView.as_view(), name='contact-us'),
    path('contact-us-success/', ContactUsSuccessTemplateView.as_view(), name='contact-us-success'),
    path('', AboutTemplateView.as_view(), name='about'),
]
