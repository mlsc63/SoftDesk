from rest_framework import permissions
from rest_framework import viewsets
from .serializers import CommentSerializer
from .models import Comments

class CommentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


    def perform_create(self, serializer):
        serializer.save(author_comment=self.request.user)
