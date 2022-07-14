from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.serializers import FoodCategorySerializer, FoodDetailSerializer, CalorieIntakeSerializer
from calories.models import CalorieCategory, CalorieFoodDetail, CalorieIntake


class FoodCaloriesListAPIView(ListAPIView):
    """ List all food details. """
    permission_classes = (permissions.AllowAny,)
    serializer_class = FoodDetailSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['food']
    search_fields = ['food']
    ordering_fields = '__all__'

    def get_queryset(self):
        return CalorieFoodDetail.objects.all()


class FoodCaloriesRetrieveAPIView(RetrieveAPIView):
    """ Retrieve food detail by food id. """
    permission_classes = (permissions.AllowAny,)
    serializer_class = FoodDetailSerializer
    queryset = CalorieFoodDetail.objects.all()


class FoodCategoriesListAPIView(ListAPIView):
    """ List all food categories. """
    permission_classes = (permissions.AllowAny,)
    serializer_class = FoodCategorySerializer
    queryset = CalorieCategory.objects.all()


class FoodCategoriesRetrieveAPIView(RetrieveAPIView):
    """ Retrieve specific food category by id. """
    permission_classes = (permissions.AllowAny,)
    serializer_class = FoodCategorySerializer
    queryset = CalorieCategory.objects.all()


class CalorieIntakeListCreateAPIView(ListCreateAPIView):
    """ Lists or Create CalorieIntake(s) """
    queryset = CalorieIntake.objects.all()
    serializer_class = CalorieIntakeSerializer


class CalorieIntakeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or destroy CalorieIntake(s) """
    queryset = CalorieIntake.objects.all()
    serializer_class = CalorieIntakeSerializer
