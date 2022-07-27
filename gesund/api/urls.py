from django.urls import path

from .views import *

urlpatterns = [

    # about us > contact us
    path('contact-us/', ContactUsListAPIView.as_view()),

    # food
    path('food-categories/', FoodCategoriesListAPIView.as_view()),
    path('food-category/<int:pk>/', FoodCategoriesRetrieveAPIView.as_view()),
    path('food-calories/', FoodCaloriesListAPIView.as_view()),
    path('food-calories/<int:pk>/', FoodCaloriesRetrieveAPIView.as_view()),

    # food
    path('calories-intake/', CalorieIntakeListCreateAPIView.as_view()),
    path('calories-intake/<int:pk>/', CalorieIntakeRetrieveUpdateDestroyAPIView.as_view()),

    path('pomodoro/', PomodoroListCreateAPIView.as_view()),
    path('pomodoro/<int:pk>/', PomodoroRetrieveUpdateDestroyAPIView.as_view()),

    # profile
    path('profile/', ProfileListCreateAPIView.as_view()),
    path('profile/<int:pk>/', ProfileRetrieveUpdateDestroyAPIView.as_view()),

    # goals
    path('goals/', GoalsListCreateAPIView.as_view()),
    path('goals/<int:pk>/', GoalsRetrieveUpdateDestroyAPIView.as_view()),

    # History
    path('history/', HistoryListAPIView.as_view()),
    path('history/<int:pk>/', HistoryRetrieveAPIView.as_view()),

    # steps
    path('steps/', StepsListCreateAPIView.as_view()),
    path('steps/<int:pk>/', StepsRetrieveUpdateDestroyAPIView.as_view()),

    # steps
    path('user-sign-log/', UserSignLogListAPIView.as_view()),

    # water intake
    path('water-intake/', WaterIntakeListCreateAPIView.as_view()),
    path('water-intake/<int:pk>/', WaterIntakeRetrieveUpdateDestroyAPIView.as_view()),

    # weights
    path('weights/', WeightListCreateAPIView.as_view()),
    path('weight/<int:pk>/', WeightRetrieveUpdateDestroyAPIView.as_view()),

    # xps
    path('xps/', XPListAPIView.as_view()),
    path('xp/<int:pk>/', XPRetrieveUpdateDestroyAPIView.as_view()),
]
