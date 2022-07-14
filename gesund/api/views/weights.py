from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.serializers import WeightSerializer
from weights.models import Weight


class WeightListCreateAPIView(ListCreateAPIView):
    """ Lists or Create weight(s). """
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer


class WeightRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or destroy weight(s). """
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer
