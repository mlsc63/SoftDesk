from rest_framework import permissions
from rest_framework import viewsets
from .serializers import IssueSerializer
from .models import Issues
from project.models import Projects
from .permission import IssuePermission


class IssueViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """

    queryset = Issues.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated & IssuePermission]

    def get_queryset(self, *args, **kwargs):
        query_project = self.kwargs.get('project_pk')
        query_issue = self.kwargs.get('pk')
        if query_issue and query_project:
            try:
                project = Projects.objects.get(pk=query_project)
                issue = Issues.objects.filter(project_id=project.id)
                issue.filter(pk=query_issue)
                return issue
            except:
                pass
        else:
            try:
                project = Projects.objects.get(pk=query_project)
                issue = Issues.objects.filter(project_id=project.id)
                return issue
            except:
                pass

    def perform_create(self, serializer):
        try:
            query_project = self.kwargs.get('project_pk')
            project = Projects.objects.get(pk=query_project)
            serializer.save(project=project)
            serializer.save(author_issue=self.request.user)
        except:
            pass

