from django.urls import path

from .views import AboutTemplateView, ContactUsCreateView, ContactUsSuccessTemplateView, ReferencesTemplateView

urlpatterns = [
    path('contact-us/', ContactUsCreateView.as_view(), name='contact-us'),
    path('contact-us-success/', ContactUsSuccessTemplateView.as_view(), name='contact-us-success'),
    path('references/', ReferencesTemplateView.as_view(), name='references'),
    path('', AboutTemplateView.as_view(), name='about'),
]
