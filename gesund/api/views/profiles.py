from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from profiles.models import Profile
from api.serializers import ProfileSerializer


class ProfileListCreateAPIView(ListCreateAPIView):
    """ Lists or create profile. """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or destroy profile. """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
