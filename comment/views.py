from rest_framework import viewsets
from .serializers import CommentSerializer
from .models import Comments
from project.models import Projects
from issue.models import Issues
from .permission import CommentPermission
from rest_framework import viewsets, permissions


class CommentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    permission_classes = [permissions.IsAuthenticated & CommentPermission]
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        query_project = self.kwargs.get('project_pk')
        query_issue = self.kwargs.get('issue_pk')
        query_comment = self.kwargs.get('pk')

        if query_project and query_issue and query_comment:
            try:
                project = Projects.objects.get(pk=query_project)
                issues = Issues.objects.filter(project=project.id)
                issue = issues.get(pk=query_issue)
                comments = Comments.objects.filter(issue=issue.id)
                comment = comments.filter(pk=query_comment)
                return comment
            except:
                pass
        elif query_project and query_issue:
            try:

                project = Projects.objects.get(pk=query_project)
                issues = Issues.objects.filter(project=project.id)
                issue = issues.get(pk=query_issue)
                comments = Comments.objects.filter(issue=issue.id)
                return comments
            except:
                pass

        else:
            pass

    def perform_create(self, serializer):
        query_project = self.kwargs.get('project_pk')
        query_issue = self.kwargs.get('issue_pk')
        if query_project and query_issue:
            try:
                project = Projects.objects.get(pk=query_project)
                issues = Issues.objects.filter(project=project.id)
                issue = issues.get(pk=query_issue)
                serializer.save(issue=issue)
                serializer.save(author_comment=self.request.user)
            except:
                pass
        else:
            pass







