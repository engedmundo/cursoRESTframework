from apps.locations.models import Location
from rest_framework.viewsets import ModelViewSet

from .serializers import LocationSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
