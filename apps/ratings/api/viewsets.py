from apps.ratings.models import Rating
from rest_framework.viewsets import ModelViewSet

from .serializers import RatingSerializer


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
