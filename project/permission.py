from rest_framework import permissions
from contributor.models import Contributor


class ProjectPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return True


    def has_object_permission(self, request, view, obj):
        query_project = view.kwargs.get("pk")

        try:
            if obj.author_project == request.user:
                return True
            elif Contributor.objects.get(user_id=request.user, project=query_project):
                return request.method in ["GET"]
            else:
                return False
        except:
            return False

    # return request.method in ["GET", "PUT", "DELETE", "POST"]