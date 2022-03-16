from apps.locations.models import Location
from rest_framework.serializers import ModelSerializer


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = [
            'id',
            'line1',
            'line2',
            'city',
            'state',
            'country',
            'latitude',
            'longitude',
        ]
