from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.serializers import ChallengeSerializer
from challenges.models import Challenge


class ChallengeListAPIView(ListAPIView):
    """ Lists all challenges. """
    serializer_class = ChallengeSerializer

    def get_queryset(self):
        return Challenge.objects.all().filter(author=self.request.user)


class ChallengeRetrieveAPIView(RetrieveAPIView):
    """ Retrieve specific challenge by id. """
    serializer_class = ChallengeSerializer

    def get_queryset(self):
        return Challenge.objects.all().filter(author=self.request.user)
