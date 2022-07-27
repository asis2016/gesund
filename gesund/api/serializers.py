from aboutus.models import ContactUs
from accounts.models import UserSignLog
from calories.models import CalorieCategory, CalorieFoodDetail, CalorieIntake
from challenges.models import Challenge
from goals.models import Goals
from history.models import History
from pomodoros.models import Pomodoro
from profiles.models import Profile
from rest_framework import serializers
from steps.models import Steps
from water_intake.models import WaterIntake
from weights.models import Weight
from xps.models import XP


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CalorieCategory
        fields = '__all__'


class FoodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalorieFoodDetail
        fields = '__all__'


class FoodCalorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalorieFoodDetail
        fields = ('id', 'food', 'description')


class CalorieIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalorieIntake
        fields = '__all__'


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'


class PomodoroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pomodoro
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class GoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goals
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'


class StepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steps
        fields = '__all__'


class UserSignLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSignLog
        fields = '__all__'


class WaterIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterIntake
        fields = '__all__'


class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = '__all__'


class XPSerializer(serializers.ModelSerializer):
    class Meta:
        model = XP
        fields = '__all__'
