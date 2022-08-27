from rest_framework import permissions


class UpdateForUserOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user and request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.method in [
            'PATCH', 'PUT', 'DELETE'
        ] and obj.username == request.user.username:
            return True


class UpdateUserPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (request.user.username == obj.username
                or (request.user.is_staff and request.user.is_superuser
                    and request.user.is_active))


class UpdateTaskPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if obj.author == request.user:
            return True
