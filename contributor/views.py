from rest_framework import viewsets, permissions
from .models import Contributor
from .serializers import ContributorSerializer
from project.models import Projects
from rest_framework.exceptions import NotFound

class ContributorViewSet(viewsets.ModelViewSet):

    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):

        query_project = self.kwargs.get('project_pk')
        project_id = Projects.objects.get(project_id=query_project)
        serializer.save(project_id_contributor=project_id)







