from rest_framework import permissions


class ProjectPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        project_id = view.kwargs.get("project_pk")
        print(project_id)

