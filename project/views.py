from rest_framework import viewsets, permissions
from .models import Projects
from contributor.models import Contributor
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer


    def perform_create(self, serializer):
        print('Create')
        serializer.save(author_project=self.request.user)

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('project_id'):
            project = Projects.objects.filter(project_id=self.kwargs.get('project_id'))
            return project
        else:
            return Projects.objects.all()









