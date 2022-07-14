from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.serializers import HistorySerializer
from history.models import History


class HistoryListAPIView(ListAPIView):
    """ Lists History. """
    queryset = History.objects.all()
    serializer_class = HistorySerializer


class HistoryRetrieveAPIView(RetrieveAPIView):
    """ Retrieve History. """
    queryset = History.objects.all()
    serializer_class = HistorySerializer
