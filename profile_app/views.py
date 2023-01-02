from rest_framework import viewsets

from profile_app.models import Profile
from profile_app.serializers import ProfileSerializer


# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Profile.objects.all()
        sort_age = self.request.query_params.get('sort_age', None)
        gender = self.request.query_params.get('gender', None)

        if gender is not None:
            queryset = queryset.filter(gender=gender)
        if sort_age is not None:
            queryset = queryset.order_by('age')
        return queryset.all()
    serializer_class = ProfileSerializer
