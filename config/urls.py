from apps.attractions.api.viewsets import AttractionViewSet
from apps.benefits.api.viewsets import BenefitViewSet
from apps.comments.api.viewsets import CommentViewSet
from apps.locations.api.viewsets import LocationViewSet
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'attractions', AttractionViewSet)
router.register(r'benefits', BenefitViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'location', LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
