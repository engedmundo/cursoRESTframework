from apps.attractions.models import Attraction
from rest_framework.serializers import ModelSerializer


class AttractionSerializer(ModelSerializer):
    class Meta:
        model = Attraction
        fields = ['id', 'name', 'description', 'approved', 'benefit']
