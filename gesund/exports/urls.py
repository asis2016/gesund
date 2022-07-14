from django.urls import path

from .views import *

urlpatterns = [
    path('food-intake', export_calories, name='export-food-intake'),
    path('steps', export_steps, name='export-steps'),
    path('water-intake', export_water_intake, name='export-water-intake'),
    path('weights', export_weights, name='export-weights'),
]
