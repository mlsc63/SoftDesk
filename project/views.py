from rest_framework import viewsets, permissions
from .models import Projects
from .serializers import ProjectSerializer
from rest_framework.generics import get_object_or_404
from contributor.models import Contributor



class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]



    def perform_create(self, serializer):
        print('Create')
        serializer.save(author_project=self.request.user)

    #def get_queryset(self, *args, **kwargs):
    #    print('ok')
    #    print(*args)
    #    print(**kwargs)
    #    user = project = self.kwargs.get("contributor")
    #    instance = Contributor.objects.filter(user_id=user)
    #    instance.delete()








