from rest_framework import permissions
from project.models import Projects
from contributor.models import Contributor


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        query_project = view.kwargs.get('project_pk')
        project = Projects.objects.get(id=query_project)
        print(query_project)
        try:
            if project.author_project == request.user:
                return True
            elif Contributor.objects.get(user_id=request.user, project=query_project):
                return request.method in ["GET"]
            else:
                return False
        except:
           return False

    def has_object_permission(self, request, view, obj):
        return True