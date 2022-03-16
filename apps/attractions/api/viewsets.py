from apps.attractions.models import Attraction
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from .serializers import AttractionSerializer


class AttractionViewSet(ModelViewSet):
    #queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Attraction.objects.filter(approved=True)
