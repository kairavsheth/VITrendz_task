from rest_framework import viewsets

from profile_app.models import Profile
from profile_app.serializers import ProfileSerializer


# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
