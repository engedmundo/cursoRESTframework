from apps.benefits.models import Benefit
from rest_framework.viewsets import ModelViewSet

from .serializers import BenefitSerializer


class BenefitViewSet(ModelViewSet):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer
