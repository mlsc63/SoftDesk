from rest_framework import viewsets, permissions
from .models import Projects
from .serializers import ProjectSerializer
from .permission import ProjectPermission


class ProjectViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated & ProjectPermission]
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer



    def get_queryset(self, *args, **kwargs):
        query_project = self.kwargs.get('pk')
        if query_project:
            try:
                project = Projects.objects.filter(id=query_project)
                return project
            except:
                pass
        else:
            project = Projects.objects.all()
            return project


    def perform_create(self, serializer):
        serializer.save(author_project=self.request.user)
















