from rest_framework import permissions
from rest_framework import viewsets
from .serializers import CommentSerializer
from .models import Comments
from project.models import Projects
from issue.models import Issues
from rest_framework.exceptions import NotFound


class CommentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


    def perform_create(self, serializer):

        try:
            query_project = Projects.objects.get(project_id=self.kwargs.get('project_pk'))
            query_issue = Issues.objects.get(project=query_project)
            serializer.save(author_comment=self.request.user)
            serializer.save(issue_id=query_issue.issue_id)

        except:
            raise NotFound("Not Found")

    def get_queryset(self, *args, **kwargs):
        query_project = self.kwargs.get('project_pk')
        query_issue = self.kwargs.get('issue_pk')
        query_comment = self.kwargs.get('pk')

        if query_issue and query_comment and query_project:
            try:
                project = Projects.objects.get(project_id=query_project)
                issue = Issues.objects.get(project=project.project_id)
                if str(issue.issue_id) == str(query_issue):
                    comment = Comments.objects.filter(issue=issue.issue_id)
                    comment.filter(comment_id=query_comment)
                    return comment
                else:
                    raise NotFound("Not found1")
            except:
                raise NotFound("Not found2")

        elif query_issue and query_project:
            try:
                project = Projects.objects.get(project _id=query_project)
                issue = Issues.objects.get(project=project.project_id)
                comment = Comments.objects.filter(issue=issue)
                if str(issue.issue_id) == str(query_issue):
                    return comment
                else:
                    raise NotFound("Not found3")
            except:
                raise NotFound("Not found4")






