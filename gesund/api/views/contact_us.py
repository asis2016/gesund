from aboutus.models import ContactUs
from api.serializers import ContactUsSerializer
from rest_framework.generics import ListAPIView


class ContactUsListAPIView(ListAPIView):
    """ Lists ContactUs. """
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
