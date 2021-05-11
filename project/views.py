from rest_framework import viewsets
from .models import Projects
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer



    def perform_create(self, serializer):
        serializer.save(author_project=self.request.user)




