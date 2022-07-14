from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.serializers import WaterIntakeSerializer
from water_intake.models import WaterIntake


class WaterIntakeListCreateAPIView(ListCreateAPIView):
    """ Lists or create water intake. """
    queryset = WaterIntake.objects.all()
    serializer_class = WaterIntakeSerializer


class WaterIntakeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or destroy water intake. """
    queryset = WaterIntake.objects.all()
    serializer_class = WaterIntakeSerializer
