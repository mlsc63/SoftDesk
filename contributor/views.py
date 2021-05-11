from rest_framework import viewsets
from .models import Contributor
from .serializers import ContributorSerializer


class ContributorViewSet(viewsets.ModelViewSet):

    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer


    def perform_create(self, serializer):
        serializer.save()
