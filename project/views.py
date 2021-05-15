from rest_framework import viewsets, permissions
from .models import Projects
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]



    def perform_create(self, serializer):
        serializer.save(author_project=self.request.user)




