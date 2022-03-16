from apps.attractions.api.viewsets import AttractionViewSet
from apps.benefits.api.viewsets import BenefitViewSet
from apps.comments.api.viewsets import CommentViewSet
from apps.locations.api.viewsets import LocationViewSet
from apps.ratings.api.viewsets import RatingViewSet
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'attractions', AttractionViewSet, basename='Attraction')
router.register(r'benefits', BenefitViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
]
