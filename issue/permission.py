from rest_framework import permissions
from contributor.models import Contributor
from project.models import Projects
from .models import Issues

class IssuePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        query_project = view.kwargs.get('project_pk')
        try:
            project = Projects.objects.get(id=query_project)
            if project.author_project == request.user:
                return True
            else:
                contributor = Contributor.objects.get(user_id=request.user, project=query_project)
                if (contributor.permission == 'CREATE') or (contributor.permission == 'ALL'):
                    return True
                elif contributor.permission == 'READ':
                    return request.method in ["GET"]
                else:
                    pass
        except:
            pass

    def has_object_permission(self, request, view, obj):
        query_project = view.kwargs.get('project_pk')
        try:
            project = Projects.objects.get(id=query_project)
            if project.author_project == request.user:
                return True
            elif Issues.objects.get(id=obj.id, author_issue=request.user):
                return True
            elif Contributor.objects.get(user_id=request.user, project=query_project):
                return True
            else:
                return False
        except:
            pass






