from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.serializers import GoalsSerializer
from goals.models import Goals


class GoalsListCreateAPIView(ListCreateAPIView):
    """ Lists or create goal(s). """
    queryset = Goals.objects.all()
    serializer_class = GoalsSerializer


class GoalsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or destroy goal(s). """
    queryset = Goals.objects.all()
    serializer_class = GoalsSerializer
