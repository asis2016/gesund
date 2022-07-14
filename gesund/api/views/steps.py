from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.serializers import StepsSerializer
from steps.models import Steps


class StepsListCreateAPIView(ListCreateAPIView):
    """ Lists or create step(s). """
    queryset = Steps.objects.all()
    serializer_class = StepsSerializer


class StepsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or destroy step(s). """
    queryset = Steps.objects.all()
    serializer_class = StepsSerializer
