from rest_framework.generics import ListAPIView

from api.serializers import XPSerializer
from xps.models import XP


class XPListAPIView(ListAPIView):
    """ Lists XPs. """
    queryset = XP.objects.all()
    serializer_class = XPSerializer
