from rest_framework import viewsets, permissions
from .models import Projects
from .serializers import ProjectSerializer
from .permission import ProjectPermission


class ProjectViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated & ProjectPermission]
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(author_project=self.request.user)
















