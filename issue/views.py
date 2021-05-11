from rest_framework import permissions
from rest_framework import viewsets
from .serializers import IssueSerializer
from .models import Issues



class IssueViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Issues.objects.all()
    serializer_class = IssueSerializer


    def perform_create(self, serializer):
        serializer.save(author_issue=self.request.user)
