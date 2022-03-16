from dataclasses import fields

from apps.benefits.models import Benefit
from rest_framework.serializers import ModelSerializer


class BenefitSerializer(ModelSerializer):
    class Meta:
        model = Benefit
        fields = ['id', 'name', 'description', 'opening_hours', 'minimum_age']
