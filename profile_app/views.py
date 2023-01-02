from rest_framework import viewsets, status
from rest_framework.response import Response

from profile_app.models import Profile
from profile_app.serializers import ProfileSerializer


# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Profile.objects.all()
        sort_age = self.request.query_params.get('sort_age', None)
        gender = self.request.query_params.get('gender', None)
        fields = self.request.query_params.get('fields', None)

        try:
            if gender is not None:
                queryset = queryset.filter(gender=gender)
            if sort_age is not None:
                queryset = queryset.order_by('age')
            if fields is not None:
                return queryset.only(*eval(fields))
            return queryset.all()
        except:
            return Response('Invalid query params', status=status.HTTP_400_BAD_REQUEST)

    serializer_class = ProfileSerializer
