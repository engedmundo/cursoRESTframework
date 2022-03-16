from apps.ratings.models import Rating
from rest_framework.serializers import ModelSerializer


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'user', 'rating', 'data']
