from rest_framework import viewsets, permissions
from .models import Contributor
from .serializers import ContributorSerializer


class ContributorViewSet(viewsets.ModelViewSet):

    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save()

    #def get_queryset(self, *args, **kwargs):
    #    print('ok')
    #    print(*args)
    #    print(**kwargs)
    #    user = project = self.kwargs.get("contributor")
    #    print(user)
    #    instance = Contributor.objects.filter(user_id=user)
    #    instance.delete()

