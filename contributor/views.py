from rest_framework import viewsets, permissions
from .models import Contributor
from .serializers import ContributorSerializer
from project.models import Projects
from .permission import UserPermission
from rest_framework.exceptions import NotFound


class ContributorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated & UserPermission]
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

    def get_queryset(self, *args, **kwargs):
        query_project = self.kwargs.get('project_pk')
        query_user = self.kwargs.get('pk')
        try:
            if query_project and query_user:
                project = Projects.objects.get(pk=query_project)
                users = Contributor.objects.filter(project=project.id)
                user = users.filter(pk=query_user)
                return user
            elif query_project:
                project = Projects.objects.get(pk=query_project)
                users = Contributor.objects.filter(project=project.id)
                return users
        except:
            raise NotFound("Something went wrong")

    def perform_create(self, serializer):

        project = Projects.objects.get(pk=self.kwargs.get('project_pk'))
        serializer.save(project=project)
