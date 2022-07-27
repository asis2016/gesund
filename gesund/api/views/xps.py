from api.serializers import XPSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from xps.models import XP


class XPListAPIView(ListAPIView):
    """ Lists XPs. """
    queryset = XP.objects.all()
    serializer_class = XPSerializer


class XPRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or destroy xp. """
    queryset = XP.objects.all()
    serializer_class = XPSerializer
