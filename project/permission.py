from rest_framework import permissions


class ProjectPermission(permissions.BasePermission):
    # READ
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return obj.author_project == request.user






    #def has_permission() -> Accés globale
    #def has_object_permission() -> Accés sur un objet

    #return True
    #return False
    #return request.method in permissions.SAFE_METHODS
