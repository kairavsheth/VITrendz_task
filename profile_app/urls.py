from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profile_app import views

router = DefaultRouter()
router.register(r'api', views.ProfileViewSet, basename="api")

urlpatterns = [
    path('', include(router.urls)),
]
