from accounts.models import UserSignLog
from api.serializers import UserSignLogSerializer
from rest_framework.generics import ListAPIView


class UserSignLogListAPIView(ListAPIView):
    """ Lists UserSignLog. """
    queryset = UserSignLog.objects.all()
    serializer_class = UserSignLogSerializer
