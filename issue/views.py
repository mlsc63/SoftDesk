from rest_framework import permissions
from rest_framework import viewsets
from .serializers import IssueSerializer
from .models import Issues
from project.models import Projects
from rest_framework.exceptions import NotFound


class IssueViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """

    queryset = Issues.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated]

    # We are looking for the project id to return it in issue
    def perform_create(self, serializer):
        try:
            project = Projects.objects.get(project_id=self.kwargs.get('project_pk'))
            serializer.save(project=project)
            serializer.save(author_issue=self.request.user)

        except Projects.DoesNotExist:
            raise NotFound(f"Project does not exist")


    def get_queryset(self, *args, **kwargs):
        # We search for the project then we compare it to issue to return it
        if self.kwargs.get('project_pk') and self.kwargs.get('pk'):
            try:
                project = self.kwargs.get('project_pk')
                issue = self.kwargs.get('pk')
                try:
                    project_query = Projects.objects.get(project_id=self.kwargs.get('project_pk'))
                except:
                    raise NotFound('Project does not exist')
                try:
                    issue_query = Issues.objects.filter(project=project_query.project_id)
                    return issue_query
                except:
                    raise NotFound('Issue does not exist, or is not attached to the right project ')
            except Issues.DoesNotExist:
                raise NotFound(f"Issue or project does not exist")


        # We are looking for the project id to return the set of issues
        elif self.kwargs.get('project_pk'):
            try:
                return Issues.objects.filter(project=self.kwargs.get('project_pk'))
            except:
                raise NotFound(f"Issue does not exist")
        else:
            raise NotFound(f"Project does not exist")




